from django.shortcuts import render
from django.http import HttpResponse
from . import models


def appointment(request):
    return render(request, 'appointments/reservation.html')


"""def test(request):
    tor.objects.create(name=request.user.username, hour=request.POST.get('hour'), min=request.POST.get('min'))
    x = tor.objects.all()
    Appointments
    return render(request, 'appointments/reservation.html', {'min': ('00', '15', '30', '45'), 'hours': range(8, 18)})
"""


