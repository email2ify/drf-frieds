from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from rest_framework.test import APIClient


"""Set up postlist"""


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Stan', password='pass')

    """ test users can list all post"""

    def test_can_list_posts(self):
        Stan = User.objects.get(username='Stan')
        Post.objects.create(owner=Stan, title='WildLife title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    """ test users can create post"""

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.post('/posts/', {'title': 'Africa Wild Life'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """ test users logged out can't create a post"""

    def test_user_not_logged_in_cant_creat_post(self):
        response = self.client.post('/posts/', {'title': 'WildLife'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


"""Set up postDetail for post id:1 and post id:2, Stan and Laurex"""


class PostDetailViewTests(APITestCase):
    def setUp(self):
        Stan = User.objects.create_user(username='Stan', password='pass')
        Laurex = User.objects.create_user(username='Laurex', password='pass')
        Post.objects.create(
            owner=Stan, title='title', content='content'
        )
        Post.objects.create(
            owner=Laurex, title='another title', content='content'
        )

    """ test valid id users to retrieve post"""

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ test invalid id users to retrieve post"""

    def test_can_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/11/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """ test users to update own post"""

    def test_user_can_update_own_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.put('/posts/1/', {'title': 'Stan new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'Stan new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ test users that can't update own post"""

    def test_user_cant_update_own_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.put('/posts/2/', {'title': 'stan new title'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    """ test users that can't update own post"""

    def test_user_can_update_own_post(self):
        self.client.login(username='Laurex', password='pass')
        response = self.client.put('/posts/2/', {'title': 'laur new title'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ test users that can't update own post"""

    def test_user_cant_update_own_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.put('/posts/2/', {'title': 'Stan new title'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    """ test users that can't delete another post"""

    def test_user_cant_delete_another_users_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.put('/posts/2/', {'title': ' new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    """ test users that can delete own post"""

    def test_user_can_delete_own_post(self):
        self.client.login(username='Stan', password='pass')
        response = self.client.put('/posts/1/', {'title': 'new title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
