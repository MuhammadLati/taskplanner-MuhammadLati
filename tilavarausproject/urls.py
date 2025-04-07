from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('reservations:room_list')),
    path('rooms/', include('reservations.urls')),
    path('login/', admin.site.urls, name='login'),
    path('logout/', admin.site.urls, name='logout'),
] 