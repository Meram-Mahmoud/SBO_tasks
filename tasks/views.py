
# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Task.objects.create( 
            title=title,
            description=description,
            status=status
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

def task_list(request):  # Initialize the tasks variable
    tasks = Task.objects.all()
    # Get filter status from request
    status_filter = request.GET.get('status')
    
    # Filter tasks by status if specified
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    paginator = Paginator(tasks, 5)  # Show 10 tasks per page
    page_number = request.GET.get('page')  # Get the current page number
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

