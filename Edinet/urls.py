"""Edinet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from Edinet.views import welcome, login, register, ClientListView, addClient
from Edinet.models import Utilisateur, Client, Info_client

urlpatterns = [
    url(r'^welcome$', welcome),
    url(r'^login$', login),
    url(r'^$', login),
    url(r'^admin/', admin.site.urls),
    url(r'^register$',register),
    url(r'^clients/', ClientListView.as_view()),
    url(r'^add-client$', addClient, name="add-cli")
]
