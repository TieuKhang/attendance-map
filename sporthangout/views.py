from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SporthangoutSerializer
from .models import Sporthangout
from .serializers import LocationinfoSerializer
from .models import LocationInfo

# Create your views here.

class SporthangoutView(viewsets.ModelViewSet):
    serializer_class = SporthangoutSerializer
    queryset = Sporthangout.objects.all()

class LocationinfoView(viewsets.ModelViewSet):
    serializer_class = LocationinfoSerializer
    queryset = LocationInfo.objects.all()
