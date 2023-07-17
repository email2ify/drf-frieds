from rest_framework import serializers
import cloudinary
from .models import Animal

class AnimalDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'description',
            'image',
            'countries',
            'slug'
        ]

    def get_image(self, obj):
        """
        Custom method to retrieve the image URL for the animal.
        Uses the CloudinaryImage class from the cloudinary package to build the URL with custom dimensions.
        """
        if obj.image and hasattr(obj.image, 'url'):
            return cloudinary.CloudinaryImage(obj.image.url).build_url(width=300, height=300, crop='fill')
        return None


class AnimalListSerializer(AnimalDetailSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        """
        Custom method to truncate the description field.
        """
        max_length = 10  # Maximum length for the truncated description
        if obj.description:
            description = (obj.description).split()
            if len(description) > max_length:
                return ' '.join(description[:max_length]) + '...'
            return obj.description
        return None


