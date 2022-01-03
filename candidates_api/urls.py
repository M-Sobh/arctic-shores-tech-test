from django.urls import path, include
from .views import api_create_candidate_view, api_get_candidate_by_ref


urlpatterns = [
    path('create-candidate/', api_create_candidate_view),
    path('get-candidate/<candidate_ref>', api_get_candidate_by_ref),

]
