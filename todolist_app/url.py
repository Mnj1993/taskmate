from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'), # 2) i made
    path('delete/<task_id>', views.delete_task, name='delete_task'), # 2) i made
    path('edit/<task_id>', views.edit_task, name='edit_task'), # 2) i made
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),

]