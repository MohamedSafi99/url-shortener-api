from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import string
import random
from django.conf import settings

def generate_short_code():
    length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def validate_url(value):
    """Custom validator to ensure the URL is valid."""
    validator = URLValidator()
    try:
        validator(value)  # Raises ValidationError if invalid
    except ValidationError:
        raise ValidationError("Invalid URL. Please enter a valid URL (e.g., https://example.com).")

class ShortenedURL(models.Model):
    original_url = models.URLField(
        max_length=2000,
        validators=[validate_url],  # Apply custom validator
        help_text="Enter a valid URL (e.g., https://example.com)."
    )
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"

    def get_short_url(self):
        return f"{settings.BASE_URL}/{self.short_code}"