from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='List of Tasks'),
    path('update_task/<str:pk>/', views.updateTask, name='Update Task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='Delete Task')
]