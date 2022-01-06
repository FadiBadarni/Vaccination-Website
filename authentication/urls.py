from django.urls import path
from . import views
from authentication import views as authentication_views

urlpatterns = [
    path('', views.home, name='Web-Home'),
    path('about/', views.about, name='About-Page'),
    path('FAQ/', views.faq, name='FAQ-Page'),
    path('contact/', views.contact, name='Contact-Page'),
    path('my_working_days/', views.my_working_days, name='my_working_days'),
    path('manage_working_days/', views.manage_working_days, name='manage_working_days'),

]

