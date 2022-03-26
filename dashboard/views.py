from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'dashboard/home.html'

class HesaplarView(ListView):
    model = models.Hesap
    context_object_name = 'hesaplar'
    template_name = 'dashboard/hesaplar.html'