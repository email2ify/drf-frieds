from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment


class CommentTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='api_test_user', password='password12345')

    def test_unauth_user_cannot_create_comment(self):

        response = self.client.post('/comments/', {'comments': 'test comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
