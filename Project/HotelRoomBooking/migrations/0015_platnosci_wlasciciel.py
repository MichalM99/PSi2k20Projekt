# Generated by Django 3.1.3 on 2021-01-21 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HotelRoomBooking', '0014_platnosci_idrezerwacji'),
    ]

    operations = [
        migrations.AddField(
            model_name='platnosci',
            name='wlasciciel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Platnosci', to='auth.user'),
            preserve_default=False,
        ),
    ]
