from django.db import models

class Klienci(models.Model):
    idKlienta = models.IntegerField(primary_key=True, null=False, unique=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

    def __str__(self):
        text = "" + self.imie + " " + self.nazwisko
        return text

class Rezerwacje(models.Model):
    numerRezerwacji = models.IntegerField(unique=True, primary_key=True, null=False)
    numerPokoju = models.ForeignKey('Pokoje',related_name='rezerwacje',on_delete=models.CASCADE)
    nazwaKlienta = models.ForeignKey('Klienci', related_name='rezerwacje', on_delete=models.CASCADE)
    dataOd = models.DateField(null=False)
    dataDo = models.DateField(null=False)
    def __str__(self):
        text = str(self.nazwaKlienta) + " " + str(self.numerPokoju)+ " " + str(self.dataOd) + " do " + str(self.dataDo)
        return text




class Platnosci(models.Model):
    idPlatnosci = models.IntegerField(unique=True, primary_key=True, null=False)
    idRezerwacji = models.ForeignKey('Rezerwacje', on_delete=models.CASCADE)
    doZaplaty = models.FloatField()
    email = models.CharField(max_length=100)

class Pokoje(models.Model):
    numerPokoju = models.IntegerField(primary_key=True, null=False, unique=True)
    liczbaMiejsc = models.IntegerField(null=False)
    cenaNetto = models.FloatField(null=False)
    def __str__(self):
        text = "" + str(self.numerPokoju) + " " + str(self.liczbaMiejsc) + "osobowy " + str(self.cenaNetto) + "pln/doba"
        return text


