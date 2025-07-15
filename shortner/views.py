from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import redirect, get_object_or_404
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

class ShortenURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def redirect_original(request, short_code):
    url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(url.original_url)