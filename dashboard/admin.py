from pyexpat import model
from django.contrib import admin
from .models import Banka, Firma, Hesap, IslemTipi

# Register your models here.
@admin.register(IslemTipi)
class IslemTipiAdmin(admin.ModelAdmin):
    list_display = ('islem_tipi', 'durum',)

@admin.register(Banka)
class BankaAdmin(admin.ModelAdmin):
    pass

@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    list_display = ('ad', 'durum',)
    filter_horizontal = ('islem_tipi',)


@admin.register(Hesap)
class HesapAdmin(admin.ModelAdmin):
    pass
