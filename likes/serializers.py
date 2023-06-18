from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):

    """Serializer for the Comment model and returning list of Comment instances"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
