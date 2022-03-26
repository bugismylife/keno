from email.policy import default
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
DURUM = (
    ("Onaylanmis", "Onaylanmis"),
    ("Reddedilen", "Reddedilen"),
    ("Bekleyen", "Bekleyen"),
)

AKTIF_PASIF = (
    ('Aktif', 'Aktif'),
    ('Pasif', 'Pasif'),
)
'''
BANKA_ADI = (
    ("Yapi Kredi", "Yapi Kredi"),
    ("Is Bankasi", "Is Bankasi"),
    ("Ziraat Bankasi", "Ziraat Bankasi"),
    ("Vakifbank", "Vakifbank"),
    ("Akbank", "Akbank"),
    ("Garanti Bankasi", "Garanti Bankasi"),
    ("Qnb Bankasi", "Qnb Bankasi"),
)
'''
class Banka(models.Model):
    banka_adi = models.CharField(max_length=30, unique=True)
    durum = models.BooleanField(default=True)

    def __str__(self):
        return self.banka_adi

    class Meta:
        verbose_name = 'Banka'
        verbose_name_plural = 'Bankalar'

class IslemTipi(models.Model):
    islem_tipi = models.CharField(max_length=50, unique=True)
    durum = models.CharField(max_length=10, choices=AKTIF_PASIF, default='Aktif')

    def __str__(self):
        return self.islem_tipi
    
    class Meta:
        verbose_name = 'Islem Tipi'
        verbose_name_plural = 'Islem Tipleri'

class Hesap(models.Model):
    # created_by = models.ForeignKey(it is gonna be user who logged in)
    banka_adi = models.ForeignKey(Banka, on_delete=models.CASCADE, related_name='hesap')
    sube_kodu = models.PositiveIntegerField(validators=[MinValueValidator(5)]) 
    hesap_no = models.PositiveIntegerField(validators=[MinValueValidator(12)])
    iban_no = models.PositiveIntegerField(validators=[MinValueValidator(24)])
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    durum = models.CharField(max_length=10, choices=AKTIF_PASIF, default='Aktif')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    max_limit = models.DecimalField(max_digits=20, decimal_places=5)
    tc_no = models.PositiveIntegerField(validators=[MinValueValidator(11)]) 
    yontem = models.ForeignKey(IslemTipi, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Hesap'
        verbose_name_plural = 'Hesaplar'

    def __str__(self):
        return f'{self.ad}-{self.soyad} {self.email}'    

class Firma(models.Model):
    ad = models.CharField(max_length=100, unique=True)
    # toplam_yatirim = models.DecimalField(max_digits=20, decimal_places=5)
    # toplam_cekim = models.DecimalField(max_digits=20, decimal_places=5)
    durum = models.CharField(max_length=10, choices=AKTIF_PASIF, default='Aktif')
    islem_tipi = models.ManyToManyField(IslemTipi, related_name='firma')
    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firmalar'
    
    def __str__(self):
        return self.ad




class Yatirim(models.Model):
    durum = models.CharField(max_length=20, choices=DURUM, default='Bekleyen')
    firma_adi = models.ForeignKey(Firma, related_name='yatirim', on_delete=models.SET_NULL, null=True)
    yatirilan_tutar = models.DecimalField(max_digits=20, decimal_places=5)
    yatirilan_hesap = models.ForeignKey(Hesap, related_name='yatirim_hesap', on_delete=models.SET_NULL, null=True)
    modified_time = models.DateField(auto_now=True)
    created_time = models.DateField(auto_now_add=True)
    # islemi alan
    # islemi aldigi tarih
    # islemi tamamladigi tarih

    def __str__(self):
        return f'{self.yatirilan_hesap.ad} {self.yatirilan_hesap.soyad}'
    # we are gonna write the module here
    class Meta:
        verbose_name = 'Yatirim'
        verbose_name_plural = 'Yatirimlar'
'''
class Cekim(models.Model):
    # we are gonna write the module here
    class Meta:
        pass

'''



