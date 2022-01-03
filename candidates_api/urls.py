from django.urls import path
from .views import create_candidate, create_score, get_candidate_by_ref

urlpatterns = [
    path('create-candidate/', create_candidate),
    path('create-score/', create_score),
    path('get-candidate/<candidate_ref>', get_candidate_by_ref)
]
