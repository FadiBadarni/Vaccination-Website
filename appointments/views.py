from django.shortcuts import render
from django.http import HttpResponse


def appointment(request):
    return render(request, 'appointments/reservation.html')


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