from django.test import TestCase
from rest_framework.test import APITestCase
from Quizzes.models import CustomUser
from .serializers import UserSerializer
import json


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        # Testing user creation via model
        user = CustomUser.objects.create_user(
            username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')


class UserSerializerTest(TestCase):
    def test_serialize_user(self):
        # Testing user serialization
        user = CustomUser.objects.create_user(
            username='testuser', password='testpassword')
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data['username'], 'testuser')

    class UserViewSetTest(APITestCase):
        def test_create_user_via_api(self):
            # Testing user creation via API
            user_data = {'username': 'testuser', 'password': 'testpassword'}
            response = self.client.post(
                '/api/users/', data=user_data, format='json')
            self.assertEqual(response.status_code, 201)  # 201 - Created
            self.assertEqual(response.data['username'], 'testuser')

    def test_retrieve_user(self):
        # Testing retrieving a user
        user = CustomUser.objects.create_user(
            username='testuser', password='testpassword')
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user(self):
        # Testing user updating
        user = CustomUser.objects.create(
            username='testuser', password='testpassword')
        updated_data = {'username': 'updateduser',
                        'password': 'updatedpassword'}
        response = self.client.put(
            f'/api/users/{user.id}/', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data.get('username', None), 'updateduser')

    def test_destroy_user(self):
        # Testing deleting user
        user = CustomUser.objects.create_user(
            username='testuser', password='testpassword')
        response = self.client.delete(f'/api/users/{user.id}/')
        # 204 NO CONTENT - successful deletion
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=user.id)
