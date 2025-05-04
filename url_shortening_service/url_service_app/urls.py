from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ShortURLViewSet

router = SimpleRouter()
router.register(r'shorturls', ShortURLViewSet, basename='shorturl')

urlpatterns = [
    path('', include(router.urls)),
]
