from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Contact


class ContactViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='api_test_user_1', password='password12345')

    def test_non_auth_user_can_post_contact(self):
        """
        Test to ensure non auth user can send a contact form
        """
        response = self.client.post('/contact/', {
            'reason': 'GENERAL',
            'name': 'tester',
            'email': 'test@post.com',
            'message': 'test contact form'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_auth_user_can_post_contact(self):
        """
        Test if user can send a contact form
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.post('/contact/', {
            'name': 'tester',
            'email': 'test@post.com',
            'message': 'test contact form'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_includes_all_required_fields(self):
        """
        To verify if contact form can be posted
        without filling in any fields 
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.post(
            '/contact/', {'message': 'Missing required fields'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

