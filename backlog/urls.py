from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TaskListAPI, TaskDetailAPI

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path("tasks/<int:task_id>/edit/", views.task_edit_model_form, name="task_edit_model_form"),
    path("tasks/<int:task_id>/toggle/", views.toggle_task_status, name="toggle_task_status"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("tasks/<int:task_id>/comment/", views.add_comment, name="add_comment"),
    path("tasks/<int:task_id>/comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
    path("debug/tasks/", views.debug_tasks, name="debug_tasks"),
    # API endpoints
    path("api/", include(router.urls)),
    path("api/task-classes/", views.get_task_classes, name="task-classes"),
]