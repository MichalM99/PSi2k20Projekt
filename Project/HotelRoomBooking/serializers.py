from rest_framework import serializers
from .models import Pokoje, Platnosci, Klienci, Rezerwacje


class KlienciSerializer(serializers.Serializer):
    class Meta:
        model = Klienci
        fields = '__all__'


class RezerwacjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezerwacje
        fields = ['numerRezerwacji', 'numerPokoju', 'dataOd', 'dataDo']


class PlatnosciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosci
        fields = ['numerRezerwacji', 'doZaplaty', 'email']


class PokojeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokoje
        fields = ['liczbaMiejsc', 'cenaNetto', 'numerPokoju']
