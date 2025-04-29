from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle_completed/<int:task_id>/', views.toggle_completed, name='toggle_completed'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
