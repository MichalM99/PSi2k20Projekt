from rest_framework import serializers
from .models import Pokoje, Platnosci, Klienci, Rezerwacje
from django.contrib.auth.models import User


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
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Platnosci
        fields = ['idPlatnosci','doZaplaty', 'email','idRezerwacji','url', 'wlasciciel']


class PokojeSerializer(serializers.HyperlinkedModelSerializer):
    rezerwacje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rezerwacje-detail')
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Pokoje
        fields = ['url','numerPokoju','liczbaMiejsc','cenaNetto','rezerwacje', 'wlasciciel']

class UserPokojeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokoje
        fields = ['numerPokoju','url']

class UserPlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platnosci
        fields = ['idPlatnosci','url']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    PokojeOwn = UserPokojeSerializer(many=True, read_only=True)
    PlatnosciOwn = UserPlatnosciSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'PlatnosciOwn', 'PokojeOwn']
