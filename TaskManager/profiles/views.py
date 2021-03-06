from django.contrib.auth import login as auth_login
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .forms import SignUpForm
from .forms import CreateTaskForm
from .forms import CreateSubtaskForm

from .models import Project as ProjectModel, Task as TaskModel, Subtask, Status


def HomeView(request):
    return render(request, 'home.html', {})


def projectview(request):
    proj = ProjectModel.objects.filter(owner=request.user)
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
    tasks = project.tasks.all().order_by('status')
    return render(request, 'tasks.html', {'project': project, 'tasks': tasks})


def task_view(request, id, task_id):
    project = get_object_or_404(ProjectModel, id=id)
    task = get_object_or_404(TaskModel, id=task_id)
    subtasks = task.subtasks.all().order_by('status')

    if request.method == 'POST':
        status_id = request.POST.get('status_id')

        task.status = status_id
        task.save()
        return redirect('project_tasks', id=project.id)

    return render(request, 'subtasks.html',
                  {'project': project, 'task': task, 'subtasks': subtasks, 'status': Status.STATUS_CHOISE})


def view_subtask(request, id, task_id, subtask_id):
    project = get_object_or_404(ProjectModel, id=id)
    task = get_object_or_404(TaskModel, id=task_id)
    subtask = get_object_or_404(Subtask, id=subtask_id)

    if request.method == 'POST':
        status_id = request.POST.get('status_id')
        subtask.status = status_id
        subtask.save()
        return redirect('task_view', id=id, task_id=task.id)

    return render(request, 'view_subtasks.html',
                  {'project': project, 'task': task, 'subtask': subtask, 'status': Status.STATUS_CHOISE})


def new_task(request, id):
    project = get_object_or_404(ProjectModel, id=id)
    user = User.objects.first()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = user
            task.status = 2
            task.save()
            return redirect('project_tasks', id=project.id)
    else:
        form = CreateTaskForm()
    return render(request, 'new_task.html', {'form': form, 'project': project})


def new_subtask(request, id, task_id):
    project = get_object_or_404(ProjectModel, id=id)
    task = get_object_or_404(TaskModel, id=task_id)
    user = User.objects.first()

    if request.method == 'POST':
        form = CreateSubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.created_by = user
            subtask.status = 2
            subtask.save()
            return redirect('task_view', id=id, task_id=task.id)
    else:
        form = CreateSubtaskForm()
    return render(request, 'new_subtask.html', {'form': form, 'task': task, 'project': project})
