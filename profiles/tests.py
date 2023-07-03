from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile



class ProfileDetailViewTests(APITestCase):
    def setUp(self):
       
        """
        Two users created to test
        """
        User.objects.create_user(username='api_test_user_1',
                                 password='password12345')
        User.objects.create_user(username='api_test_user_2',
                                 password='password12345')

    def test_user_can_view_existing_profile(self):
        
        """
        Test to view existing user profile
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_non_existing_profile(self):
        
        """
        Test to view profile which that does not exist
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
    def test_user_can_update_owned_profile(self):
       
        """
        Test user can update their profile when not logged in
        """
        response = self.client.put('/profiles/1/',
                                   {'name': 'mark'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)    
     
    
    def test_user_can_update_owned_profile(self):
        
        """
        Test user that can update a profile they own
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.put('/profiles/1/',
                                   {'name': 'pin'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'pin')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_profiles(self):
       
        """
        Test user cannot update other users profiles
        """
        self.client.login(username='api_test_user_1', password='password12345')
        response = self.client.put('/profiles/2/', {'name': 'mark'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
