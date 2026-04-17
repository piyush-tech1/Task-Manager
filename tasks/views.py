from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import redirect
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required #This ia a decoarator, it means if the user is not login dont even run this view, redirect them to login.

def task_list(request): #Show all tasks for logged in user.
    tasks = Task.objects.filter(user=request.user) #Each user sees only their own tasks.
    return render(request, 'tasks/task_list.html',{'tasks':tasks})
    #request-> pass the request, 'tasks/task_list.html'-> which template to use, {tasks:tasks}-> Data sends to template

@login_required
def task_complete(request, task_id): #Mark a task as done.
    task = Task.objects.get(id = task_id) #find the task
    task.done = True #update it
    task.save() #save to database
    return redirect('task_list') #send user back

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('task_list')

@login_required
def task_create(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('task_list')
    else:
        form= TaskForm()
    return render(request, 'tasks/task_create.html',{'form':form})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html',{'form':form})
            