from django.shortcuts import render,redirect

from .models import *
from .forms import *

# Create your views here.

def index(request):
    print("4")
    tasks = Task.objects.all()
    print(tasks)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks , 'form':form}
    return render(request, 'tasks/lists.html',context)


def updateTask(request, id):
    task = Task.objects.get(id = id)

    form = TaskForm(instance= task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html',context)


def deleteTask(request, id):
    item = Task.objects.get(id = id)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html',{'item':item})
