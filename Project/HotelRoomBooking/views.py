from django.shortcuts import render
from django.http import HttpResponse

from .serializers import KlienciSerializer, RezerwacjeSerializer, PokojeSerializer, PlatnosciSerializer, UserSerializer
from .models import Klienci, Pokoje, Platnosci, Rezerwacje
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from django_filters import AllValuesFilter, DateFilter, FilterSet, NumberFilter
from django.contrib.auth.models import User



class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-list'
    filter_fields=['imie','nazwisko']
    search_fields=['imie', 'nazwisko','idKlienta']
    ordering_fields = ['imie', 'nazwisko', 'idKlienta']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class KlienciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)

class PlatnosciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'platnosci-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RezerwacjeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rezerwacje.objects.all()
    serializer_class = RezerwacjeSerializer
    name = 'rezerwacje-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)

class PokojeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokoje.objects.all()
    serializer_class = PokojeSerializer
    name = 'pokoje-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'







class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'klienci': reverse(KlienciList.name, request=request),
                         'pokoje': reverse(PokojeList.name, request=request),
                         'platnosci': reverse(PlatnosciList.name, request=request),
                         'rezerwacje': reverse(RezerwacjeList.name, request=request),
                         'Uzytkownicy': reverse(UserList.name, request=request),
                         })