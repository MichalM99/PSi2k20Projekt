from django.shortcuts import render
from django.http import HttpResponse
from .serializers import KlienciSerializer, RezerwacjeSerializer, PokojeSerializer, PlatnosciSerializer
from .models import Klienci, Pokoje, Platnosci, Rezerwacje
from rest_framework import viewsets




class KlienciViewSet(viewsets.ModelViewSet):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer