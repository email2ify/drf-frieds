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


"""
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_friends.permissions import IsOwnerOrReadOnly




class ProfileList(APIView):
   
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

        """
