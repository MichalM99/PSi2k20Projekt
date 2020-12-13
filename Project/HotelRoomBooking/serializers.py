from rest_framework import serializers
from .models import Pokoje, Platnosci, Klienci, Rezerwacje


class KlienciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klienci
        fields = ['numerRezerwacji','numerPokoju', 'imie', 'nazwisko', 'email','url']


class RezerwacjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezerwacje
        fields = ['numerRezerwacji', 'numerPokoju', 'dataOd', 'dataDo','url']


class PlatnosciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosci
        fields = ['numerRezerwacji', 'doZaplaty', 'email','url']


class PokojeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokoje
        fields = ['liczbaMiejsc', 'cenaNetto', 'numerPokoju','url']
