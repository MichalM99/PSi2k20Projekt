# Generated by Django 3.1.3 on 2021-01-03 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelRoomBooking', '0005_auto_20210103_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienci',
            name='rezerwacje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rezerwa', to='HotelRoomBooking.rezerwacje'),
        ),
    ]