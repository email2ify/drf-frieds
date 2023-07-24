from django.db.models import Q

from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalListSerializer, AnimalDetailSerializer


class AnimalList(generics.ListAPIView):
    serializer_class = AnimalListSerializer
    queryset = Animal.objects.all()


class AnimalDetail(generics.RetrieveAPIView):
    serializer_class = AnimalDetailSerializer
    queryset = Animal.objects.all()
    lookup_field = 'slug'


class AnimalsByCountryList(generics.ListAPIView):
    serializer_class = AnimalListSerializer

    def get_queryset(self):
        # Retrieve the country from the captured URL parameter
        country = self.kwargs['country']

        # Filter animals based on the country parameter
        queryset = Animal.objects.filter(countries__contains=country)

        # Raise a NotFound exception if no animals exists for the country
        if not queryset.exists():
            error_message = f"No animals found for country '{country}'."
            raise NotFound(detail=error_message)

        return queryset


class CountriesWithAnimalsList(generics.ListAPIView):
    serializer_class = None  # We don't need a serializer for this simple list

    def get_queryset(self):
        # Get all animals that have at least one country associated with them
        animals_with_countries = Animal.objects.exclude(countries=[])

        # Extract the unique countries from the animals and sort them alphabetically
        countries = set()
        for animal in animals_with_countries:
            countries.update(animal.countries)

        sorted_countries = sorted(list(countries))

        return sorted_countries

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class AnimalSearchView(generics.ListAPIView):
    serializer_class = AnimalListSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')

        # Filter by or country
        if query:
            return Animal.objects.filter(
                Q(name__icontains=query)
            )

        # Return all animals if no search parameters provided
        return Animal.objects.all()
