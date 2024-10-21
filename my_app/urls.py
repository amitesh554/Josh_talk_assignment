from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/assign/', views.assign_task, name='assign_task'),
    path('users/<int:user_id>/tasks/', views.get_tasks_for_user, name='get_tasks_for_user'),
]