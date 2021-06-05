from django.db import models

class Todo(models.Model):
    """todo list model"""
    todo_item = models.CharField(max_length=200)

    def __str__(self):
        return self.todo_item
