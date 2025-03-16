from django.urls import path
from .views import (
    task_edit_model_form, task_list, task_detail, toggle_task_status, delete_task, debug_tasks, add_comment, delete_comment
)

urlpatterns = [
    path("", task_list, name="task_list"),
    path("<int:task_id>/", task_detail, name="task_detail"),
    path("<int:task_id>/edit/", task_edit_model_form, name="task_edit_model_form"),
    path("<int:task_id>/toggle/", toggle_task_status, name="toggle_task_status"),
    path("<int:task_id>/delete/", delete_task, name="delete_task"),
    path("debug/", debug_tasks, name="debug_tasks"),
    path("<int:task_id>/comment/add/", add_comment, name="add_comment"),
    path("<int:task_id>/comment/<int:comment_id>/delete/", delete_comment, name="delete_comment"),
]