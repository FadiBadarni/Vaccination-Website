from django.shortcuts import render
from django.views.generic import CreateView


def home(request):
    return render(request, 'authentication/home.html')


def about(request):
    return render(request, 'authentication/about.html')


def faq(request):
    return render(request, 'authentication/FAQ.html')


def contact(request):
    return render(request, 'authentication/contact_form.html')




