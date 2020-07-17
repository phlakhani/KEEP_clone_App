from django.urls import path
from .views import index, updateTask, deleteTask

urlpatterns = [
    path('', index, name='list'),
    path('updateTask/<int:pk>', updateTask, name='updateTask'),
    path('deleteTask/<int:pk>', deleteTask, name='deleteTask')
]
