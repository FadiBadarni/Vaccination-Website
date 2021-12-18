from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.core.mail import send_mail


def register(request):

    # check if request is of type post (user register)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        # check if form received is valid
        if form.is_valid():
            form.save()     # Save the user



            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered For {username} .')       # Flash message usage with f_string
            return redirect('login')   # Redirect user to home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # Render register with form


@login_required    # Decorator to add restrictions to profile view
# @allowed_users(allowed_roles=['admin'])
def profile(request):
    return render(request, 'users/profile.html')


