from django.urls import path
from . import views_horoscope

urlpatterns = [
    path('type', views_horoscope.index_types),
    path('', views_horoscope.index, name='horoscope-index'),
    path('<int:sign_zodiak>', views_horoscope.get_info_about_zodiak_by_number),
    path('<str:sign_zodiak>', views_horoscope.get_info_about_zodiak, name='horoscope-name'),
    path('type/<sign_zodiak>', views_horoscope.index_types_lvl2),
]
