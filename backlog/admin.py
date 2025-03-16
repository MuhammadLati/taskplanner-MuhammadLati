from django.contrib import admin
from .models import Task, TaskClass, Comment

@admin.register(TaskClass)
class TaskClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_class', 'user', 'priority', 'completed')
    list_filter = ('task_class', 'completed', 'priority', 'user')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'content', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('content', 'user__username', 'task__title')