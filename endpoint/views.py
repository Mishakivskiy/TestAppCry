from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .serializers import CarsDataSerializer


class CarsDataListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'horse_power']
