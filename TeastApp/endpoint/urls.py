from django.urls import path
from .views import CarsDataListAPIView


urlpatterns = [
    path('cars/', CarsDataListAPIView.as_view(), name='cars_data_api'),
]