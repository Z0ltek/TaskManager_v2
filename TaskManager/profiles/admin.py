from django.contrib import admin
from .models import Project
from .models import Task
from .models import Subtask
from .models import Permissions


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Permissions)
