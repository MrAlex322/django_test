from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

days_dict = {
    'monday': "Много работаю",
    'tuesday': "Работаю много",
    'wednesday': "Работаю много",
    'thursday': "Работаю не так много",
    'friday': "Работаю мало",
    'saturday': "Чилю много",
    'sunday': "Чилю мало",
}


def index_days(request):
    days = list(days_dict)
    # days_element += f"<li><a href='{redirect_path_days}'>{day}</a></li>"
    contex_days_week = {
        'days_week': days
    }
    return render(request,'week_days/index_days.html', context=contex_days_week)


def get_info_about_days_of_week(request, sign_days: str):
    disctription_days = days_dict.get(sign_days)
    data_days = {
       'disctription_week_days': disctription_days
    }
    return render(request,'week_days/greeting.html', context=data_days)



def get_info_about_days_of_week_by_number(request, sign_days: int):
    days = list(days_dict)
    if sign_days > len(days):
        return HttpResponseNotFound(f"Неверный номер дня - {sign_days}")
    numbers_days = days[sign_days - 1]
    redirect_days = reverse("week_days_name", args=(numbers_days, ))
    return HttpResponseRedirect(redirect_days)
