from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^projects/$', views.projectview, name='projects'),
    url(r'^projects/(?P<id>\d+)/$', views.project_tasks, name='project_tasks'),
    url(r'^projects/(?P<id>\d+)/new/$', views.new_task, name='new_task'),
    url(r'^projects/(?P<id>\d+)/task/(?P<task_id>\d+)/$', views.task_view, name='task_view'),
    url(r'^projects/(?P<id>\d+)/task/(?P<task_id>\d+)/(?P<subtask_id>\d+)/$', views.view_subtask, name='view_subtask'),
    url(r'^projects/(?P<id>\d+)/task/(?P<task_id>\d+)/new/$', views.new_subtask, name='new_subtask'),

]
