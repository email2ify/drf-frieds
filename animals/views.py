from django.db.models import Q

from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalListSerializer, AnimalDetailSerializer


class AnimalList(generics.ListAPIView):
    """
    Returns a list of all animals.
    """
    serializer_class = AnimalListSerializer
    queryset = Animal.objects.all()


class AnimalDetail(generics.RetrieveAPIView):
    """
    Returns the details of a specific animal based on its unique slug.
    """
    serializer_class = AnimalDetailSerializer
    queryset = Animal.objects.all()
    lookup_field = 'slug'


class AnimalsByCountryList(generics.ListAPIView):
    """
    Returns a list of animals associated with a specific country.
    """

    serializer_class = AnimalListSerializer

    def get_queryset(self):
        """
        Retrieve the country from the captured URL parameter and
        filter animals based on the country parameter.
        """
        country = self.kwargs['country']
        queryset = Animal.objects.filter(countries__contains=country)

        return queryset


class CountriesWithAnimalsList(generics.ListAPIView):
    """
    Returns a sorted list of countries that are associated with at least one animal.
    """

    serializer_class = None  # A serializer is not needed for this simple list

    def get_queryset(self):
        """
        Get all animals that have at least one country associated with them
        and extract the unique countries from them, sorted alphabetically.
        """

        animals_with_countries = Animal.objects.exclude(countries=[])

        countries = set()
        for animal in animals_with_countries:
            countries.update(animal.countries)

        sorted_countries = sorted(list(countries))

        return sorted_countries

    def list(self, request, *args, **kwargs):
        """
        Handle GET requests and return the sorted list of countries as the response.
        """
        queryset = self.get_queryset()
        return Response(queryset)


class AnimalSearchView(generics.ListAPIView):
    """
    Search for animals based on a query string (q parameter).
    """
    serializer_class = AnimalListSerializer

    def get_queryset(self):
        """
        Get the search query from the request parameters
        and filter animals based on the name containing the query.
        """
        query = self.request.query_params.get('q')
        if query:
            return Animal.objects.filter(
                Q(name__icontains=query)
            )

        # Raise a NotFound exception if no search parameters are provided
        raise NotFound('No search parameters provided.')

    def list(self, request, *args, **kwargs):
        """
        Handle GET requests
        and return a list of animals that match the search query.
        """
        queryset = self.get_queryset()

        # Raise a NotFound exception if no animals are found
        if not queryset.exists():
            error_message = "No animals found with the given search parameters '{}'".format(
                self.request.query_params.get('q')
            )
            raise NotFound(error_message)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
