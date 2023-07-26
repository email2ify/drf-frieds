from rest_framework import serializers
import cloudinary
from .models import Animal

class AnimalDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed representation of a specific animal.
    """
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
        if obj.image:
            # transformations to apply to images
            transformations = "c_fill,h_350,w_600"
            image_url = obj.image.url
            # Find the index of "upload/" in the image URL
            upload_index = image_url.find("upload/")

            if upload_index != -1:
                # Use str.replace to insert the transformations after "upload/"
                transformed_url = image_url.replace("upload/", f"upload/{transformations}/", 1)
                return transformed_url

        return None


class AnimalListSerializer(AnimalDetailSerializer):
    """
    Serializer for listing animals with truncated descriptions and transformed image URLs.
    """
    description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

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

    def get_image(self, obj):
        """
        Method to apply transformation to images
        """
        if obj.image:
            # transformations to apply to images
            transformations = "c_fill,h_650,w_650,g_face,ar_1.0"
            image_url = obj.image.url
            # Find the index of "upload/" in the image URL
            upload_index = image_url.find("upload/")

            if upload_index != -1:
                # Use str.replace to insert the transformations after "upload/"
                transformed_url = image_url.replace("upload/", f"upload/{transformations}/", 1)
                return transformed_url

        return None


