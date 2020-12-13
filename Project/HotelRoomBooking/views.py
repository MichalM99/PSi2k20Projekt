from django.shortcuts import render
from django.http import HttpResponse
from .serializers import KlienciSerializer, RezerwacjeSerializer, PokojeSerializer, PlatnosciSerializer
from .models import Klienci, Pokoje, Platnosci, Rezerwacje
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse



class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-list'

class KlienciDetail(generics.RetrieveDestroyAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-detail'

class PlatnosciList(generics.ListCreateAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'platnosci-list'

class PlatnosciDetail(generics.RetrieveDestroyAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'Platnosci-detail'

class RezerwacjeList(generics.ListCreateAPIView):
    queryset = Rezerwacje.objects.all()
    serializer_class = RezerwacjeSerializer
    name = 'rezerwacje-list'

class RezerwacjeDetail(generics.RetrieveDestroyAPIView):
    queryset = Rezerwacje.objects.all()
    serializer_class = RezerwacjeSerializer
    name = 'rezerwacje-detail'

class PokojeList(generics.ListCreateAPIView):
    queryset = Pokoje.objects.all()
    serializer_class = PokojeSerializer
    name = 'Pokoje-list'

class PokojeDetail(generics.RetrieveDestroyAPIView):
    queryset = Pokoje.objects.all()
    serializer_class = PokojeSerializer
    name = 'Pokoje-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'klienci': reverse(KlienciList.name, request=request),
                         'pokoje': reverse(PokojeList.name, request=request),
                         'platnosci': reverse(PlatnosciList.name, request=request),
                         'rezerwacje': reverse(RezerwacjeList.name, request=request),

                         })