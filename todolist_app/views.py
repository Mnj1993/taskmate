from django.core import paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages .success(request,("New Task Added!"))    
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks,10)
        page = request.GET.get('pg')
        all_tasks= paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks' : all_tasks } ) # 4)8) I made, Jinja2

    
    #context = {
    #    'Welcome_text':"Welcom to todo list page", #9)  I made
    #}
    # 3) return HttpResponse("welcome to Task page")

@login_required
def  delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("Access restricted"))

    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task edited!"))    
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj' : task_obj } )

@login_required
def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("Access restricted"))
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    context = {
        'index_text':"Welcome to index page", #11)  I made
    }
    return render(request, 'index.html', context )

def contact(request):
    context = {
        'contact_text':"Welcom to contact us page", #11)  I made
    }
    return render(request, 'contact.html', context )

def about(request):
    context = {
        'about_text':"Welcom to about us page", #11)  I made
    }
    return render(request, 'about.html', context )
