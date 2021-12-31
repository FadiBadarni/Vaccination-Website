from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import DoctorRegisterForm
from django.http import HttpResponse
from .decorators import allowed_users
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def register_type(request):
    return render(request, 'users/register_type.html')


def register_doctor(request):
    return render(request, 'users/register_doctor.html')


def register(request):
    # check if request is of type post (user register)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        # check if form received is valid
        if form.is_valid():
            form.save()  # Save the user

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered For {username} .')  # Flash message usage with f_string
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # Render register with form

@csrf_exempt
def register_doctor(request):
    # check if request is of type post (user register)
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)

        # check if form received is valid
        if form.is_valid():
            form.save()  # Save the user

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered For {username} .')  # Flash message usage with f_string
            return redirect('login')
    else:
        form = DoctorRegisterForm()
    return render(request, 'users/register_doctor.html', {'form': form})  # Render register with form


@login_required  # Decorator to add restrictions to profile view
# @allowed_users(allowed_roles=['admin'])
def profile(request):
    return render(request, 'users/profile.html')
