from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import *
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.test import Client
from django.contrib.auth.models import User


# Create your tests here.

class KlienciTests(APITestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        self.user.save()
        self.client.login(username='test', password='test')

    def post_klient(self, idKlienta, imie, nazwisko, email):
        url = reverse(views.KlienciList.name)
        data = {'idKlienta':idKlienta,'imie':imie,'nazwisko':nazwisko,'email': email}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_klient(self):
        new_klient_id = 2
        new_klient_imie = 'Michal'
        new_klient_nazwisko = 'Moszczynski'
        new_klient_email = 'michalmoszczynski99@gmail.com'
        response = self.post_klient(new_klient_id, new_klient_imie, new_klient_nazwisko, new_klient_email)
        print("PK {0}".format(Klienci.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Klienci.objects.count() == 1
        assert Klienci.objects.get().idKlienta == new_klient_id
        assert Klienci.objects.get().imie == new_klient_imie
        assert Klienci.objects.get().nazwisko == new_klient_nazwisko
        assert Klienci.objects.get().email == new_klient_email

    def test_post_existing_klient(self):
        new_idKlienta = 2
        data = {'idKlienta':new_idKlienta}
        response_one = self.post_klient(new_idKlienta,'test','test','test')
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_klient(new_idKlienta,'test2','test2','test2')
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_klient_by_nazwisko(self):
        idKlienta1 = 3
        idKlienta2 = 4
        nazwisko1 = 'Maciaszek'
        nazwisko2 = 'Kononowicz'
        self.post_klient(idKlienta1, 'test', nazwisko1, 'test')
        self.post_klient(idKlienta2, 'test', nazwisko2, 'test')
        filter_by_name = {'nazwisko': nazwisko1}
        url= '{0}?{1}'.format(reverse(views.KlienciList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwisko'] == nazwisko1

    def test_get_klienci_collection(self):
        new_idKlienta = 8
        self.post_klient(new_idKlienta, 'test', 'test', 'test')
        url = reverse(views.KlienciList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['idKlienta'] == new_idKlienta


    def test_update_klient(self):
        new_idKlienta = 18
        new_imie = 'Czarek'
        new_nazwisko = 'Wesoly'
        new_email = 'wesolutkiczarek@gmail.com'
        response = self.post_klient(new_idKlienta, new_imie, new_nazwisko, new_email)
        url = urls.reverse(views.KlienciDetail.name,None,{response.data['idKlienta']})
        upd_idKlienta = 99
        upd_imie = 'George'
        upd_nazwisko = 'Sad'
        upd_email = 'sadgeorge@gmail.com'
        data = {'idKlienta': upd_idKlienta,'imie':upd_imie,'nazwisko' : upd_nazwisko, 'email':upd_email}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['idKlienta'] == upd_idKlienta
        assert patch_response.data['imie'] == upd_imie
        assert patch_response.data['nazwisko'] == upd_nazwisko
        assert patch_response.data['email'] == upd_email


    def test_get_klient(self):
        new_idKlienta = 18
        new_imie = 'Czarek'
        new_nazwisko = 'Wesoly'
        new_email = 'wesolutkiczarek@gmail.com'
        response = self.post_klient(new_idKlienta, new_imie, new_nazwisko, new_email)
        url = urls.reverse(views.KlienciDetail.name,None,{response.data['idKlienta']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['idKlienta'] == new_idKlienta
        assert get_response.data['imie'] == new_imie
        assert get_response.data['nazwisko'] == new_nazwisko
        assert get_response.data['email'] == new_email


class PokojeTests(APITestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        self.user.save()
        self.client.login(username='test', password='test')

    def post_pokoj(self, numerPokoju, liczbaMiejsc, cenaNetto):
        url = reverse(views.PokojeList.name)
        data = {'numerPokoju':numerPokoju,'liczbaMiejsc':liczbaMiejsc,'cenaNetto':cenaNetto}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_pokoj(self):
        new_numerPokoju = 202
        new_liczbaMiejsc = 2
        new_cenaNetto = 300
        response = self.post_pokoj(new_numerPokoju, new_liczbaMiejsc, new_cenaNetto)
        print("PK {0}".format(Pokoje.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Pokoje.objects.count() == 1
        assert Pokoje.objects.get().numerPokoju == new_numerPokoju
        assert Pokoje.objects.get().liczbaMiejsc == new_liczbaMiejsc
        assert Pokoje.objects.get().cenaNetto == new_cenaNetto

    def test_post_existing_pokoj(self):
        new_numerPokoju = 303
        response_one = self.post_pokoj(new_numerPokoju,3, 400)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_pokoj(new_numerPokoju, 2, 300)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_pokoje_collection(self):
        new_numerPokoju = 183
        self.post_pokoj(new_numerPokoju, 2, 150)
        url = reverse(views.PokojeList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['numerPokoju'] == new_numerPokoju

    def test_update_pokoj(self):
        new_numerPokoju = 101
        new_liczbaMiejsc = 3
        new_cenaNetto = 450
        response = self.post_pokoj(new_numerPokoju, new_liczbaMiejsc, new_cenaNetto)
        url = urls.reverse(views.PokojeDetail.name,None,{response.data['numerPokoju']})
        upd_liczbaMiejsc = 4
        upd_cenaNetto = 500
        data = {'liczbaMiejsc': upd_liczbaMiejsc,'cenaNetto':upd_cenaNetto}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['numerPokoju'] == new_numerPokoju
        assert patch_response.data['liczbaMiejsc'] == upd_liczbaMiejsc
        assert patch_response.data['cenaNetto'] == upd_cenaNetto

    def test_get_klient(self):
        new_numerPokoju = 101
        new_liczbaMiejsc = 3
        new_cenaNetto = 450
        response = self.post_pokoj(new_numerPokoju, new_liczbaMiejsc, new_cenaNetto)
        url = urls.reverse(views.PokojeDetail.name,None,{response.data['numerPokoju']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['numerPokoju'] == new_numerPokoju
        assert get_response.data['liczbaMiejsc'] == new_liczbaMiejsc
        assert get_response.data['cenaNetto'] == new_cenaNetto
