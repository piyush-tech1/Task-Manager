from django.urls import path
from .import views

urlpatterns=[
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('signup', views.signup, name='signup'),
]