from django.shortcuts import render
from django.http import HttpResponse

from .serializers import KlienciSerializer, RezerwacjeSerializer, PokojeSerializer, PlatnosciSerializer
from .models import Klienci, Pokoje, Platnosci, Rezerwacje
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateFilter, FilterSet, NumberFilter



class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-list'
    filter_fields=['imie','nazwisko']
    search_fields=['imie', 'nazwisko','idKlienta']
    ordering_fields = ['imie', 'nazwisko', 'idKlienta']

class KlienciDetail(generics.RetrieveDestroyAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-detail'

class PlatnosciFilter(FilterSet):
    from_doZaplaty = NumberFilter(field_name='doZaplaty', lookup_expr='gte', label='Do zapłaty od: ')
    to_doZaplaty = NumberFilter(field_name='doZaplaty', lookup_expr='lte', label='Do zapłaty do: ')

    class Meta:
        model = Platnosci
        fields = ['from_doZaplaty', 'to_doZaplaty']


class PlatnosciList(generics.ListCreateAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'platnosci-list'
    search_fields=['idRezerwacji', 'email']
    ordering_fields = ['idRezerwacji','doZaplaty']
    filter_class = PlatnosciFilter

class PlatnosciDetail(generics.RetrieveDestroyAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'platnosci-detail'

class RezerwacjeFilter(FilterSet):
    from_dataOd = DateFilter(field_name='dataOd', lookup_expr='gte', label='Data rozpoczęcia pobytu od: ')
    to_dataOd = DateFilter(field_name='dataOd', lookup_expr='lte', label='Data rozpoczęcia pobytu do: ')
    from_dataDo = DateFilter(field_name='dataDo', lookup_expr='gte', label='Data zakonczenia pobytu od: ')
    to_dataDo = DateFilter(field_name='dataDo', lookup_expr='lte', label='Data zakonczenia pobytu do: ')

    class Meta:
        model = Rezerwacje
        fields = ['from_dataOd', 'to_dataOd', 'from_dataDo', 'to_dataDo']

class RezerwacjeList(generics.ListCreateAPIView):
    queryset = Rezerwacje.objects.all()
    serializer_class = RezerwacjeSerializer
    name = 'rezerwacje-list'
    filter_fields=['nazwaKlienta']
    search_fields=['dataOd', 'dataDo','nazwaKlienta','numerRezerwacji']
    ordering_fields = ['nazwaKlienta','numerPokoju']
    filter_class = RezerwacjeFilter

class RezerwacjeDetail(generics.RetrieveDestroyAPIView):
    queryset = Rezerwacje.objects.all()
    serializer_class = RezerwacjeSerializer
    name = 'rezerwacje-detail'


class PokojeFilter(FilterSet):
    from_liczbaMiejsc = NumberFilter(field_name='liczbaMiejsc', lookup_expr='gte', label='Liczba miejsc od: ')
    to_liczbaMiejsc = NumberFilter(field_name='liczbaMiejsc', lookup_expr='lte', label='Liczba miejsc do: ')
    class Meta:
        model = Pokoje
        fields = ['from_liczbaMiejsc']


class PokojeList(generics.ListCreateAPIView):
    queryset = Pokoje.objects.all()
    serializer_class = PokojeSerializer
    name = 'pokoje-list'
    filter_class = PokojeFilter
    search_fields=['numerPokoju','liczbaMiejsc']
    ordering_fields = ['cenaNetto','liczbaMiejsc','numerPokoju']

class PokojeDetail(generics.RetrieveDestroyAPIView):
    queryset = Pokoje.objects.all()
    serializer_class = PokojeSerializer
    name = 'pokoje-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'klienci': reverse(KlienciList.name, request=request),
                         'pokoje': reverse(PokojeList.name, request=request),
                         'platnosci': reverse(PlatnosciList.name, request=request),
                         'rezerwacje': reverse(RezerwacjeList.name, request=request),

                         })