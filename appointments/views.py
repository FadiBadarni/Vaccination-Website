from django.shortcuts import render
from django.http import HttpResponse


def appointment(request):
    return render(request, 'appointments/reservation.html')



