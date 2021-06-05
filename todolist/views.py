from django.shortcuts import render
from .models import Todo
from django import forms


class TodoForm(forms.Form):
    todo = forms.CharField()

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = form.cleaned_data['todo']
    
            todo = Todo(todo_item=todo_item)
            todo.save()

    todo_items = Todo.objects.all()
    context = {'todos': todo_items, 'my_form': TodoForm()}
    return render (request, 'todolist/index.html', context)

# def add_todo(request):
    

 