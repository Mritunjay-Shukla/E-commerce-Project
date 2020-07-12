from django.shortcuts import render
from django.contrib.auth import get_user_model
from account.forms import SignupForm 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.conf import settings
# Create your views here.

class Signup(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form): 
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return
        
