from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    return render(request, 'authentication/home.html')


def about(request):
    return render(request, 'authentication/about.html')


def faq(request):
    return render(request, 'authentication/FAQ.html')


class ContactCreate(CreateView):
    model = Contact
    fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy("contact_recieved")


def contact_recieved(request):
    return render(request, 'authentication/contact_recieved.html')
