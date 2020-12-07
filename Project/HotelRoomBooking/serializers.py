from rest_framework import serializers
from HotelRoomBooking import Pokoje, Platnosci, Rezerwacje, Klienci


class KlienciSerializer(serializers.Serializer):
    class Meta:
        model = Klienci
        fields = ['numerRezerwacji','numerPokoju','imie', 'nazwisko', 'email']


class RezerwacjeSerializer(serializers.Serializer):
    class Meta:
        model = Rezerwacje
        fields = ['numerRezerwacji', 'numerPokoju', 'dataOd', 'dataDo']


class PlatnosciSerializer(serializers.Serializer):
    class Meta:
        model = Platnosci
        fields = ['numerRezerwacji', 'doZaplaty', 'email']


class PokojeSerializer(serializers.Serializer):
    class Meta:
        model = Pokoje
        fields = ['liczbaMiejsc', 'cenaNetto', 'numerPokoju']
