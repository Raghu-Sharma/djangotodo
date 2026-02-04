from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('todo_list')

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo_list')

def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')
