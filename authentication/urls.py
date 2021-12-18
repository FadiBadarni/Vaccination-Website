from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Web-Home'),
    path('about/', views.about, name='About-Page'),
    path('contact/', views.contact, name='Contact-Us'),
]

