from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.make_reservation, name='make_reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
] 