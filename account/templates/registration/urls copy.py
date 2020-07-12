"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mstore.views import homepage
from django.conf import settings
from django.conf.urls.static import static
from mstore.views import product_detail, category, search
from account.views import Signup
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('product/<int:id>', product_detail),
    path('category/<str:category>', category),
    path('search/', search, name='searchbar'),
    path("account/register", Signup.as_view()),
    path("login",LoginView.as_view(template_name="registration/login.html")),
    path('password_reset/', PasswordResetView.as_view()),
    path('password_reset/done/', PasswordResetDoneView.as_view()),
    path('password_reset_complete/', PasswordResetCompleteView.as_view()),
    path('', include('django.contrib.auth.urls'))


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
