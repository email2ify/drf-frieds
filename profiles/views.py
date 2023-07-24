from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_friends.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):

    """create view as profile and creation is handled by django signals."""

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),

    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'posts_count',

    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):

    """crud functionality for profile if user is owner."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),

    ).order_by('-created_at')
    serializer_class = ProfileSerializer

