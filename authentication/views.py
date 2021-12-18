from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'authentication/home.html')


def about(request):
    return render(request, 'authentication/about.html')
def contact(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
        [email], fail_silently=False)
        return render(request, 'authentication/emailsent.html', {'email': email})

    return render(request, 'authentication/contact.html', {})




