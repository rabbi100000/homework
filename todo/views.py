from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


@api_view(['GET'])
def todo(request):
    person1 = {
        'name': 'Rabbi',
        'age': 19,
        'phone': '245673',
    }

    person2 = {
        'name': 'nissain',
        'age': 19,
        'phone': '245673',
    }
    person_list = [person1, person2]
    return Response(person_list)

@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoListSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request,id):
    todo = get_object_or_404(Todo,id=id)
    serializer = TodoDetailSerializer(todo)
    return Response(serializer.data)