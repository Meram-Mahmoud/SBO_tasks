
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
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    
    # Get the filter status from the request
    status_filter = request.GET.get('status', '')
    
    # Filter tasks by status if a filter is applied
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Pagination setup - 5 tasks per page
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Render the template with the page_obj containing filtered tasks
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        # Update the task object with the new values
        task.title = title
        task.description = description
        task.status = status
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

