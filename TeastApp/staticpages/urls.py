from django.urls import path
from .views import api_documentation


urlpatterns = [
    path('documentation/', api_documentation, name='api_documentation'),
]
