from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment, Post


class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='api_test_user', password='password12345')
        self.post1 = Post.objects.create(owner=self.user, title='title', content='content')
        self.post2 = Post.objects.create(owner=self.user, title='title 2', content='content 2')
        self.comment = Comment.objects.create(content='test comment', owner=self.user, post=self.post1)
        self.comment2 = Comment.objects.create(content='test comment 2', owner=self.user, post=self.post2)

    def test_unauth_user_cannot_create_comment(self):
        """Unauthenticated user should not be able to create a comment."""
        response = self.client.post('/comments/', {'comments': 'test comment'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_auth_user_can_create_comment(self):
        """Authenticated user should be able to create a comment."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/comments/',
            {'comments': 'test comment', 'post': self.post1.id, 'content': 'test content'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_comments(self):
        """List all comments."""
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_filter_comments_by_post(self):
        """Filter comments by post."""
        Comment.objects.create(owner=self.user, content='comment 1', post=self.post1)
        Comment.objects.create(owner=self.user, content='comment 2', post=self.post2)
        response = self.client.get('/comments/', {'post': self.post1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve_comment(self):
        """Retrieve a specific comment."""
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_own_comment(self):
        """Authenticated owner should be able to update their comment."""
        self.client.force_authenticate(user=self.user)
        updated_comment_data = {'comments': 'updated comment','content': 'Updated comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', updated_comment_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_own_comment(self):
        """Authenticated owner should be able to delete their comment."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
