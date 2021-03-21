from django.shortcuts import redirect, render
from user . models import Profile
from . models import Todo
from . forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def base(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def addtasks(request):
    todos = Todo.objects.filter(user = request.user).order_by('is_completed')
    if request.method == "POST":
        task_title = request.POST['task_title']
        todos = Todo(
            task_title = task_title,
            user = request.user
        )
        todos.save()
        return redirect('tasks')
    data = {
        'todos':todos,
    }
    return render(request, 'index.html',data)

@login_required(login_url='login')
def editTask(request, id):
    task = Todo.objects.get(pk = id)
    todo = TaskForm(instance=task)
    if request.method == 'POST':
        todo = TaskForm(request.POST, instance=task)
        if todo.is_valid():
            todo.save()
            return redirect('tasks')
    data = {
        'todo':todo,
    }
    return render(request, 'edit.html', data)

def delete(request, id):
    todo = Todo.objects.get(pk  = id)
    if request.method == "POST":
        todo.delete()
        return redirect('tasks')

    data = {
        'todo':todo,
    }
    return render(request, 'delete.html', data)