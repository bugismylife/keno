# Generated by Django 4.0.3 on 2022-03-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_firma_islem_tipi_islemtipi_firma_adi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islemtipi',
            name='firma_adi',
            field=models.ManyToManyField(related_name='firmalar', to='dashboard.firma'),
        ),
    ]
