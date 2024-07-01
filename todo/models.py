from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length= 544)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now= True)
    updated_at = models.DateField(auto_now= True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)