from django.db import models

class Klienci(models.Model):
    numerRezerwacji = models.IntegerField(unique=True, primary_key=True, null=False)
    numerPokoju = models.IntegerField(null=False)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

class Rezerwacje(models.Model):
    numerRezerwacji = models.IntegerField(unique=True, primary_key=True, null=False)
    numerPokoju = models.ForeignKey('Pokoje',on_delete=models.CASCADE)
    dataOd = models.DateTimeField(null=False)
    dataDo = models.DateTimeField(null=False)

class Platnosci(models.Model):
    numerRezerwacji = models.IntegerField(unique=True, primary_key=True, null=False)
    doZaplaty = models.FloatField()
    email = models.CharField(max_length=100)

class Pokoje(models.Model):
    liczbaMiejsc = models.IntegerField(null=False)
    cenaNetto = models.FloatField(null=False)
    numerPokoju = models.IntegerField(primary_key=True, null=False, unique=True)