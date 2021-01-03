from rest_framework import serializers
from .models import Pokoje, Platnosci, Klienci, Rezerwacje


class KlienciSerializer(serializers.HyperlinkedModelSerializer):
    rezerwacje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rezerwacje-detail')
    class Meta:
        model = Klienci
        fields = ['url','idKlienta', 'imie', 'nazwisko', 'email','rezerwacje']


class RezerwacjeSerializer(serializers.HyperlinkedModelSerializer):
    #nazwaKlienta = serializers.SlugRelatedField(queryset=Klienci.objects.all(), slug_field='nazwisko')
    class Meta:
        model = Rezerwacje
        fields = ['numerRezerwacji', 'numerPokoju','nazwaKlienta','dataOd', 'dataDo','url']


class PlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platnosci
        fields = ['idPlatnosci','doZaplaty', 'email','idRezerwacji','url']


class PokojeSerializer(serializers.HyperlinkedModelSerializer):
    rezerwacje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rezerwacje-detail')
    class Meta:
        model = Pokoje
        fields = ['url','numerPokoju','liczbaMiejsc','cenaNetto','rezerwacje']