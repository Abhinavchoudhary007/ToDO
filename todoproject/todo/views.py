from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# View to display the home page with task list and handle adding new tasks
def index(request):
    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                tasks = Task.objects.all().order_by('-creation_time')
                return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})
        elif 'completed_task' in request.POST:
            form = TaskForm()
            tasks = Task.objects.filter(completed=True).order_by('-creation_time')
            return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})
    else:
        form = TaskForm()
        tasks = Task.objects.filter(completed=False).order_by('-creation_time')
    return render(request, 'todo/index.html', {'form': form, 'tasks': tasks})

# View to toggle the completed status of a task
def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

# View to display completed tasks on a separate page
def completed_tasks(request):
    tasks = Task.objects.filter(completed=True).order_by('-creation_time')
    return render(request, 'todo/completed_tasks.html', {'tasks': tasks})

# View to edit an existing task
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

# View to delete a completed task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('completed_tasks')
