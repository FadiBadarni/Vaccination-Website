from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Web-Home'),
    path('about/', views.about, name='About-Page'),
    path('FAQ/', views.faq, name='FAQ-Page'),
    path('contact/', views.contact, name='Contact-Page'),
    # path("contact_recieved/", contact_recieved, name="contact_recieved"),
    # path("contact_recieved/home/", views.home),
]
