from rest_framework import serializers
from .models import *

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        exclude = ['updated_at','completed']
        depth = 1

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        fields ='__all__'     
        depth = 1 