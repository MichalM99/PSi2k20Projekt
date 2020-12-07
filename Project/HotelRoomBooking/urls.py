from . import views
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'klienci', views.KlienciViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]