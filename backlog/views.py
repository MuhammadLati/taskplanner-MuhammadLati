from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from .models import Task, TaskClass, Comment
from .forms import TaskEditModelForm

@login_required
def task_list(request):
    """Retrieve all tasks grouped by task class."""
    task_classes = ['Todo', 'In progress', 'Done', 'Backlog']
    
    grouped_tasks = {}
    for category in task_classes:
        # Filter tasks based on user permissions
        if request.user.is_superuser or request.user.is_staff:
            tasks = Task.objects.filter(task_class__title=category).order_by('-priority')
        else:
            tasks = Task.objects.filter(
                task_class__title=category,
                user=request.user  # Only show tasks belonging to the current user
            ).order_by('-priority')
        grouped_tasks[category.lower().replace(" ", "_")] = tasks

    context = {
        'grouped_tasks': grouped_tasks,
        'is_admin': request.user.is_superuser or request.user.is_staff
    }
    return render(request, 'backlog/task_list.html', context)

@login_required
def task_detail(request, task_id):
    """Display details of a specific task."""
    try:
        task = get_object_or_404(Task, id=task_id)
        
        # Check if user has permission to view this task
        if not (request.user.is_superuser or request.user.is_staff) and task.user != request.user:
            return HttpResponseForbidden("Et voi tarkastella tätä tehtävää.")
            
        return render(request, 'backlog/task_detail.html', {'task': task})
    except Http404:
        # Redirect to task list with an error message if task doesn't exist
        from django.contrib import messages
        messages.error(request, f"Tehtävää ID:llä {task_id} ei löydy.")
        return redirect('task_list')

@login_required
def task_edit_model_form(request, task_id):
    """Edit a task using model form or create a new one if task_id is 0."""
    if task_id == 0:
        # Creating a new task
        task = None
    else:
        # Editing existing task
        task = get_object_or_404(Task, id=task_id)
        # Check if user has permission to edit this task
        if not (request.user.is_superuser or request.user.is_staff) and task.user != request.user:
            return HttpResponseForbidden("Et voi muokata tätä tehtävää.")
    
    if request.method == 'POST':
        form = TaskEditModelForm(request.POST, instance=task)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user  # Always assign the current user
            new_task.save()
            return redirect('task_list')
    else:
        form = TaskEditModelForm(instance=task)
    
    return render(request, 'backlog/task_edit_form.html', {
        'form': form, 
        'task': task,
        'is_new': task_id == 0
    })

@login_required
def toggle_task_status(request, task_id):
    """Toggle the completed status of a task."""
    task = get_object_or_404(Task, id=task_id)
    
    # Check if user has permission to toggle this task
    if not (request.user.is_superuser or request.user.is_staff) and task.user != request.user:
        return HttpResponseForbidden("Et voi muokata tätä tehtävää.")
        
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    """Delete a task."""
    task = get_object_or_404(Task, id=task_id)
    
    # Check if user has permission to delete this task
    if not (request.user.is_superuser or request.user.is_staff) and task.user != request.user:
        return HttpResponseForbidden("Et voi poistaa tätä tehtävää.")
        
    task.delete()
    return redirect('task_list')

@login_required
def debug_tasks(request):
    """Debug view to list all tasks and their IDs."""
    if not request.user.is_superuser:
        return HttpResponseForbidden("Vain ylläpitäjät voivat nähdä tämän sivun")
        
    tasks = Task.objects.all().select_related('user', 'task_class')
    return render(request, 'backlog/debug_tasks.html', {'tasks': tasks})

@login_required
def add_comment(request, task_id):
    """Add a comment to a task."""
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                task=task,
                user=request.user,
                content=content
            )
    return redirect('task_detail', task_id=task.id)

@login_required
def delete_comment(request, task_id, comment_id):
    """Delete a comment."""
    comment = get_object_or_404(Comment, id=comment_id, task_id=task_id)
    
    # Check if user has permission to delete this comment
    if not request.user.is_superuser and comment.user != request.user:
        return HttpResponseForbidden("Et voi poistaa tätä kommenttia.")
        
    comment.delete()
    return redirect('task_detail', task_id=task_id)