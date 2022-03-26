from django.urls import path
from .views import HomeTemplateView, HesaplarView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('hesaplar/', HesaplarView.as_view(), name='hesaplar'),
]