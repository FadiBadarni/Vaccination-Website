from django.shortcuts import render
from django.http import HttpResponse


def appointment(request):
    return render(request, 'appointments/reservation.html')

def my_appointments(request):
    return render(request, 'appointments/my-appointments.html')

@user_not_confined
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

@allowed_users(allowed_roles=['admin'])
def list_all_appointments(request):
    appointments = Appointment.objects.all().order_by('-date_created')
    context = {'appointments': appointments}
    return render(request, 'appointments/list-all-appointments.html', context)

@allowed_users(allowed_roles=['doctor'])
def list_appointments(request):
    appointments = Appointment.get_appoinments_except_day(request.user.profile.holiday).order_by('-date_created')
    context = {'appointments': appointments}
    return render(request, 'appointments/list-appointments.html', context)

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
    return render(request, 'appointments/working-days.html',context)