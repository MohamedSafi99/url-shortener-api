from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'created_at']
        read_only_fields = ['short_code', 'short_url', 'created_at']

    def get_short_url(self, obj):
        return obj.get_short_url()

    def validate_original_url(self, value):
        """Ensures the URL is valid before saving."""
        validator = URLValidator()
        try:
            validator(value)  # Raises ValidationError if invalid
        except ValidationError:
            raise serializers.ValidationError("Invalid URL. Please enter a valid URL (e.g., https://example.com).")
        return value