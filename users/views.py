from multiprocessing import context
from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout

from . import forms
# Create your views here.
class LoginView(View):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
   
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username, password)
            print(user)
            if user is not None:
                login(request, authenticate)
                return redirect('dashboard:home')
        message = 'Giris bilgileri hatalidir'
        return render(request, self.template_name, context={'form': form, 'message': message})