from django.urls import path
from .views import *

urlpatterns = [
    path('',todo, name='todo'),
    path('todos/',todo_list, name='todo_list'),
    path('todo/<int:id>/',todo_detail, name='todo_detail')
]
