from django.urls import path, include
from .views import api_create_candidate_view


urlpatterns = [
    path('create-candidate/', api_create_candidate_view),

]
