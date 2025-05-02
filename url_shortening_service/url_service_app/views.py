from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404

class CreateShortURL(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class RetrieveShortURL(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.access_count += 1
        short_url.save()
        serializer = ShortURLSerializer(short_url)
        return Response(serializer.data)

class UpdateShortURL(APIView):
    def put(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteShortURL(APIView):
    def delete(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class URLStats(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(short_url)
        return Response(serializer.data)
