from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from drf_friends.permissions import IsOwnerOrReadOnly
from .models import User1
from .serializers import User1Serializer


class User1List(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = User1Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Calculate the total number of reviews and an average rating
    # related to each User1.
    queryset = User1.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'speciality',
        'location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = User1Serializer
    queryset = User1.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')