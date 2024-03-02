from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# https://www.homeenglish.ru/OtherGoroscop.htm - описание знако зодиака
# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
    'fire': ['aries','leo','sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

# Выводим список всех знаков


def index(request):
    zodiacs = list(zodiac_dict)
    # li_element += f"<li><a href='{redirect_path}'>{sign}</a></li>"
    context_zodiac = {
        'zodiacs': zodiacs
    }
    return render(request,'horoscope/index.html',context=context_zodiac)

# Выводим список видов знаков


def index_types(request):
    types_zodiacs = list(types)
    li_element_types = ''
    for var in types_zodiacs:
        li_element_types += f"<li><a href='/horoscope/type/{var}'>{var}</a></li>"
    response_type = f"""
    <ol>
        {li_element_types}
    </ol>
    """
    return HttpResponse(response_type)

# Выводим спиок знаков, принадлежащих к конректному виду


def index_types_lvl2(request, sign_zodiak):
    name_types = types.get(sign_zodiak, None)
    if name_types:
        i_elem = ''
        for item in name_types:
            redirect_path = reverse("horoscope-name", args=(item,))
            i_elem += f"<li><a href='{redirect_path}'>{item}</a></li>"
        response_types_2 = f"""
        <ul>
            {i_elem}
        </ul>
        """
        return HttpResponse(response_types_2)
    else:
        return HttpResponseNotFound(f"Неизвестный тип - {sign_zodiak}")


#Выводим информацию о знаке (принимаем строку в качестве аргумента)


def get_info_about_zodiak(request, sign_zodiak: str):
    description = zodiac_dict.get(sign_zodiak)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiak,
        'sign_name' : description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


#Выводим информацию о знаке, принимая число в качестве аргумента и перенаправляем запрос

def get_info_about_zodiak_by_number(request, sign_zodiak: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f"Неверный номер задиака - {sign_zodiak}")
    name_zodiac = zodiacs[sign_zodiak - 1]
    redirect_name = reverse("horoscope-name", args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_name)
