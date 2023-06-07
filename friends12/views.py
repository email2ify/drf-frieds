from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):

    def get(self, request):
        friends12 = Profile.objects.all()
        serializer = ProfileSerializer(friends12, many=True)
        return Response(serializer.data)