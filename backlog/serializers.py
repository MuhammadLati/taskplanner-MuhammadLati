from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'task_class', 'priority', 'user', 'additional_info']
        read_only_fields = ['user'] 