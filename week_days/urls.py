from django.urls import path
from . import views_week_days


urlpatterns = [
    path('', views_week_days.index_days),
    path('<int:sign_days>', views_week_days.get_info_about_days_of_week_by_number),
    path('<str:sign_days>', views_week_days.get_info_about_days_of_week, name='week_days_name'),
]