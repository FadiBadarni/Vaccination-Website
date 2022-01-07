# Create your tests here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from users.forms import ManageHolidayForm
from .models import Appointment
from .models import WEEK_DAYS
from users.decorators import allowed_users
import datetime


def appointment(request):
    return render(request, 'appointments/reservation.html')



def my_appointments(request):
    return render(request, 'appointments/my-appointments.html')


@allowed_users(allowed_roles=['admin'])
def list_all_appointments(request):
    appointments = Appointment.objects.all().order_by('-date_created')
    context = {'appointments': appointments}
    return render(request, 'appointments/list-all-appointments.html', context)


@allowed_users(allowed_roles=['doctor'])
def list_appointments(request):
    appointments = Appointment.objects.filter(status = False).order_by('-date_created')
    context = {'appointments': appointments}
    return render(request, 'appointments/list-appointments.html', context)


@allowed_users(allowed_roles=['admin'])
def manage_working_days(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id", None)
        doctors = User.objects.filter(groups__name='doctor')
        user = get_object_or_404(User, id = user_id)
        form = ManageHolidayForm(request.POST)
        if form.is_valid():
            holiday = form.cleaned_data["holiday"]
            user.profile.holiday = holiday
            user.profile.save()
            messages.success(request, "Holiday updated successfully")
        context = {'doctors': doctors, 'form': form}
    if request.method == "GET":
        doctors = User.objects.filter(groups__name='doctor')
        form = ManageHolidayForm()
        context = {'doctors': doctors, 'form': form}
    return render(request, 'appointments/manage-working-days.html', context)


@allowed_users(allowed_roles=['doctor'])
def manage_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id", None)
        action = request.POST.get("action", None)
        appointment = get_object_or_404(Appointment, id = appointment_id)
        if action == "cancel":
            appointment.delete()
            messages.success(request, "Appointment Cancelled Successfully")
        elif action == "vaccinated":
            appointment.vaccinated_by = request.user
            appointment.status = True
            appointment.save()
            messages.success(request, "Vaccinated Successfully")
    previous_url = request.META.get('HTTP_REFERER', None)
    if previous_url:
        return redirect(previous_url)
    return redirect("Web-Home")


@allowed_users(allowed_roles=['doctor'])
def my_working_days(request):
    working_days = []
    holidays = []
    for day in WEEK_DAYS:
        if day[0] == request.user.profile.holiday:
            holidays.append(day[1])
        else:
            working_days.append(day[1])
    context = {'working_days': working_days, 'holidays': holidays}
    return render(request, 'appointments/working-days.html', context)


def book_appointment(request):
    day = request.GET.get("day", None)
    time = request.GET.get("time", None)
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    time = datetime.time(hour=int(hour), minute=int(minute))
    if Appointment.is_time_available(time, day):
        Appointment.objects.create(
            user = request.user,
            time = time,
            day = day,
        )
        messages.success(request, f"Appointment Booked Successfully For {time}.")
    else:
        messages.error(request, f"Appointment Already Booked.")
    return redirect('appointment')


def unbook_appointment(request):
    appointment_id = request.GET.get("ap_id", None)
    appointment = get_object_or_404(Appointment, id = appointment_id)
    if appointment.user == request.user:
        appointment.delete()
        messages.success(request, f"Appointment UnBooked Successfully.")
    else:
        return HttpResponseForbidden()
    return redirect('appointment')



