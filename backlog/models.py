from django.db import models
from django.contrib.auth.models import User

class TaskClass(models.Model):
    title = models.CharField(max_length=100)  # "Todo", "In Progress", "Done", etc.
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Task Classes"

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    task_class = models.ForeignKey(TaskClass, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'

    class Meta:
        ordering = ['-created_at']  # Show newest comments first