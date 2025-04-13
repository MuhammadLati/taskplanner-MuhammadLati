from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Import Django Auth Views
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("task_list")),  # ✅ Redirect '/' to task_list
    path("tasks/", include("backlog.urls")),  # ✅ Ensure backlog app's URLs are included
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Muutettu template_name
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),  # ✅ Logout URL
    # Add the API URLs
    path('', include('backlog.urls')),
]