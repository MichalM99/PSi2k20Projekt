# Generated by Django 3.1.3 on 2021-01-03 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelRoomBooking', '0012_auto_20210103_0522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rezerwacje',
            old_name='numerKlienta',
            new_name='nazwaKlienta',
        ),
    ]
