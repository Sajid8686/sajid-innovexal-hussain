from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = 'short_code'

    def retrieve(self, request, short_code=None):
        short_url = self.get_object()
        short_url.access_count += 1
        short_url.save()
        serializer = self.get_serializer(short_url)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='stats')
    def stats(self, request, short_code=None):
        short_url = self.get_object()
        serializer = self.get_serializer(short_url)
        return Response(serializer.data)
