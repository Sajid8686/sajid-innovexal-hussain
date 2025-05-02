from django.urls import path
from .views import *

urlpatterns = [
    path('shorten', CreateShortURL.as_view(), name='create-short-url'),
    path('shorten/<str:short_code>', RetrieveShortURL.as_view(), name='retrieve-url'),
    path('shorten/<str:short_code>/update', UpdateShortURL.as_view(), name='update-url'),
    path('shorten/<str:short_code>/delete', DeleteShortURL.as_view(), name='delete-url'),
    path('shorten/<str:short_code>/stats', URLStats.as_view(), name='url-stats'),
]

