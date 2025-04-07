from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from reservations.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('reservations:room_list')),
    path('rooms/', include('reservations.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasks/', include('backlog.urls')),  # Keep existing tasks URLs
    path('register/', register, name='register'),
]