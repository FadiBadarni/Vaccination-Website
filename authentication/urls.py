from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Web-Home'),
    path('about/', views.about, name='About-Page'),
    path('FAQ/', views.faq, name='FAQ-Page'),
    path('contact/', views.contact, name='Contact-Page'),
    path("contact_recieved/", contact_recieved, name="contact_recieved"),
     path("contact_recieved/home/", views.home),
path('', views.appointment, name='appointment'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('unbook_appointment/', views.unbook_appointment, name='unbook_appointment'),
    path('list_all_appointments/', views.list_all_appointments, name='list_all_appointments'),
    path('list_appointments/', views.list_appointments, name='list_appointments'),
]
