from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from Quizzes.models import CustomUser
from .serializers import UserSerializer


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        # Test the creation of a user through the model
        user = CustomUser.objects.create_user(username='testuser', password='password')
        self.assertEqual(user.username, 'testuser')


class UserSerializerTest(TestCase):
    def test_serialize_user(self):
        # Test the serialization of a user
        user = CustomUser.objects.create_user(username='user', password='password')
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data['username'], 'user')


class UserViewSetTest(APITestCase):
    def setUp(self):
        # Set up the test client and create a superuser
        self.client = APIClient()
        self.admin_user = CustomUser.objects.create_superuser(username='admin', email='admin@example.com', password='password')

    def test_create_user_via_api(self):
        # Test the creation of a user through the API
        user_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/users/', data=user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')

    def test_retrieve_user(self):
        # Test retrieving a user through the API
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user(self):
        # Test updating a user through the API
        user = CustomUser.objects.create(username='testuser', password='testpassword')
        updated_data = {'username': 'updateduser', 'password': 'updatedpassword'}
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(f'/api/users/{user.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('username', None), 'updateduser')

    def test_destroy_user(self):
        # Test deleting a user through the API
        user = CustomUser.objects.create_user(username='test', password='password')
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=user.id)
