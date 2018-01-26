from django.contrib.auth import login as auth_login
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .forms import SignUpForm
from .forms import CreateTaskForm

from .models import Project as ProjectModel, Task as TaskModel, Subtask, Status

def HomeView(request):
    return render(request, 'home.html', {})

def projectview(request):
    proj = ProjectModel.objects.all()
    return render(request, 'projects.html', {'proj': proj})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def LogoutView(request):
    logout(request)

def project_tasks(request, id):
    project = get_object_or_404(ProjectModel, id=id)
    task = TaskModel.objects.all()
    return render(request, 'tasks.html', {'project': project, 'task': task})

def new_task(request, id):
    project = get_object_or_404(ProjectModel, id=id)
    user = User.objects.first()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = user
            task.status = 1
            task.save()
            return redirect('project_tasks', id=project.id)
    else:
        form = CreateTaskForm()
    return render(request, 'new_task.html', {'form': form, 'project': project})










