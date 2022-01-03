from django.urls import path
from django.urls.resolvers import URLPattern
from .views import create_candidate

urlpatterns = [
    path('create-candidate/', create_candidate)
]
