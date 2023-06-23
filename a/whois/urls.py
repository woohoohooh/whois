from django.urls import path
from . import views

urlpatterns = [
    path('', views.whois, name='whois'),
]