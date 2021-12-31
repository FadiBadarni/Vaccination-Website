from django.shortcuts import render
from .models import Appointment


def appointment(request):
    return render(request, 'appointments/reservation.html')


def test(request):
    Appointment.objects.create(name=request.user.username, hour=request.POST.get('hour'), min=request.POST.get('min'))
    x = Appointment.objects.all()
    return render(request, 'appointments/reservation.html',
                  {'min': ('00', '15', '30', '45'), 'hours': range(8, 18), 'Appointment': x})
