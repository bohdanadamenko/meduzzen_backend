from django.test import TestCase


class HomePageTest(TestCase):
    # Test case for the home page of the application

    def test_home_page_status_code(self):
        # Test to ensure that the home page is accessible and returns a 200 status code
        response = self.client.get('/')
        self.assertEqual(response.status_code, 300)
