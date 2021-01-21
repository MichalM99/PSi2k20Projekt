from . import views
from django.urls import path
from . import views



urlpatterns = [
    path('klienci', views.KlienciList.as_view(), name=views.KlienciList.name),
    path('klienci/<int:pk>', views.KlienciDetail.as_view(), name=views.KlienciDetail.name),
    path('pokoje', views.PokojeList.as_view(), name=views.PokojeList.name),
    path('pokoje/<int:pk>', views.PokojeDetail.as_view(), name=views.PokojeDetail.name),
    path('rezerwacje', views.RezerwacjeList.as_view(), name=views.RezerwacjeList.name),
    path('rezerwacje/<int:pk>', views.RezerwacjeDetail.as_view(), name=views.RezerwacjeDetail.name),
    path('platnosci', views.PlatnosciList.as_view(), name=views.PlatnosciList.name),
    path('platnosci/<int:pk>', views.PlatnosciDetail.as_view(), name=views.PlatnosciDetail.name),
    path('uzytkownicy', views.UserList.as_view(), name=views.UserList.name),
    path('uzytkownicy/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]