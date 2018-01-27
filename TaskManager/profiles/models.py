from django.db import models
from django.contrib.auth.models import User

class Status():
    INPROGRESS = 1
    TODO = 2
    DONE = 3

    STATUS_CHOISE = (
        (TODO, 'TODO'),
        (INPROGRESS, 'IN PROGRESS'),
        (DONE, 'DONE')
    )

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=4000)
    last_updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='project')

    def __str__(self):
        return self.name

    def get_tasks_count(self):
        return Task.objects.filter(task__project=self).count()

    def get_last_update(self):
        return Task.objects.filter(task__project=self).order_by('-created_at').first()

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.IntegerField(Status, choices=Status.STATUS_CHOISE)
    project = models.ForeignKey(Project, related_name='tasks')
    time = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='tasks')
    owner = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.name

class Subtask(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(max_length=4000)
    status = models.IntegerField(Status, choices=Status.STATUS_CHOISE)
    task = models.ForeignKey(Task, related_name='subtasks')
    time = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='subtasks')
    owner = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.name
