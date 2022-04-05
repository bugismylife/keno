# Generated by Django 4.0.3 on 2022-03-26 16:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banka_adi', models.CharField(max_length=30, unique=True)),
                ('durum', models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], default='Aktif', max_length=10)),
            ],
            options={
                'verbose_name': 'Banka',
                'verbose_name_plural': 'Bankalar',
            },
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, unique=True)),
                ('durum', models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], default='Aktif', max_length=10)),
            ],
            options={
                'verbose_name': 'Firma',
                'verbose_name_plural': 'Firmalar',
            },
        ),
        migrations.CreateModel(
            name='Hesap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sube_kodu', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5)])),
                ('hesap_no', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(12)])),
                ('iban_no', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(24)])),
                ('ad', models.CharField(max_length=100)),
                ('soyad', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('durum', models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], default='Aktif', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('max_limit', models.DecimalField(decimal_places=5, max_digits=20)),
                ('tc_no', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(11)])),
                ('banka_adi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hesap', to='dashboard.banka')),
            ],
            options={
                'verbose_name': 'Hesap',
                'verbose_name_plural': 'Hesaplar',
            },
        ),
        migrations.CreateModel(
            name='IslemTipi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('islem_tipi', models.CharField(max_length=50, unique=True)),
                ('durum', models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], default='Aktif', max_length=10)),
            ],
            options={
                'verbose_name': 'Islem Tipi',
                'verbose_name_plural': 'Islem Tipleri',
            },
        ),
        migrations.CreateModel(
            name='Yatirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum', models.CharField(choices=[('Onaylanmis', 'Onaylanmis'), ('Reddedilen', 'Reddedilen'), ('Bekleyen', 'Bekleyen')], default='Bekleyen', max_length=20)),
                ('yatirilan_tutar', models.DecimalField(decimal_places=5, max_digits=20)),
                ('ucret', models.DecimalField(decimal_places=5, default=0.0, max_digits=20)),
                ('modified_time', models.DateField(auto_now=True)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0')),
                ('aktarim_tipi', models.CharField(choices=[('Api', 'Api'), ('Manuel', 'Manuel'), ('Aktarilmamis', 'Aktarilmamis')], default='Aktarilmamis', max_length=30)),
                ('banka_adi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yatirimlar', to='dashboard.banka')),
                ('firma_adi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yatirim', to='dashboard.firma')),
                ('yatirilan_hesap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yatirim_hesap', to='dashboard.hesap')),
            ],
            options={
                'verbose_name': 'Yatirim',
                'verbose_name_plural': 'Yatirimlar',
            },
        ),
        migrations.AddField(
            model_name='hesap',
            name='yontem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.islemtipi'),
        ),
        migrations.AddField(
            model_name='firma',
            name='islem_tipi',
            field=models.ManyToManyField(related_name='firma', to='dashboard.islemtipi'),
        ),
    ]
