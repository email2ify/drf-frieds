from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Animal
from .serializers import AnimalListSerializer, AnimalDetailSerializer


class TestAnimalList(APITestCase):
    """
    Test case for the AnimalList API view.
    """

    def setUp(self):
        self.animal1 = Animal.objects.create(name="Lion", countries=["Kenya", "Tanzania"])
        self.animal2 = Animal.objects.create(name="Elephant", countries=["Kenya"])

    def test_get_animal_list(self):
        """
        Test the GET request to retrieve the animal list.
        """
        url = reverse("animal-list")
        response = self.client.get(url)
        
        animals = Animal.objects.all()
        serializer = AnimalListSerializer(animals, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)


class TestAnimalDetail(APITestCase):
    """
    Test case for the AnimalDetail API view.
    """

    def setUp(self):
        self.animal = Animal.objects.create(name="Lion", countries=["Kenya", "Tanzania"])

    def test_get_animal_detail(self):
        """
        Test the GET request to retrieve the details of a specific animal.
        """
        url = reverse("animal-detail", kwargs={"slug": self.animal.slug})
        response = self.client.get(url)
        serializer = AnimalDetailSerializer(self.animal)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_nonexistent_animal_detail(self):
        """
        Test the GET request for a non-existent animal detail.
        """
        url = reverse("animal-detail", kwargs={"slug": "nonexistent"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestAnimalsByCountryList(APITestCase):
    """
    Test case for the AnimalsByCountryList API view.
    """

    def setUp(self):
        self.animal1 = Animal.objects.create(name="Lion", countries=["Kenya", "Tanzania"])
        self.animal2 = Animal.objects.create(name="Elephant", countries=["Kenya"])

    def test_get_animals_by_country(self):
        """
        Test the GET request to retrieve the list of animals for a specific country.
        """
        url = reverse("animals-by-country", kwargs={"country": "Kenya"})
        response = self.client.get(url)
        animals = Animal.objects.filter(countries__contains="Kenya")
        serializer = AnimalListSerializer(animals, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_nonexistent_country(self):
        """
        Test the GET request for a non-existent country.
        """
        url = reverse("animals-by-country", kwargs={"country": "Nonexistent"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_empty_animals_list_for_country(self):
        """
        Test the GET request for an empty list of animals for a specific country.
        """
        url = reverse("animals-by-country", kwargs={"country": "Malawi"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
