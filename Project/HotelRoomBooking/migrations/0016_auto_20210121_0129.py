# Generated by Django 3.1.3 on 2021-01-21 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HotelRoomBooking', '0015_platnosci_wlasciciel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platnosci',
            name='wlasciciel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlatnosciOwn', to=settings.AUTH_USER_MODEL),
        ),
    ]
