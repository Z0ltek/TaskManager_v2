from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project
from .models import Task
from .models import Subtask
from .models import Status


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Project
        fields = ('name', 'description')


class CreateTaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Task
        fields = ('name', 'description')


class CreateSubtaskForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Subtask
        fields = ('name', 'message')
