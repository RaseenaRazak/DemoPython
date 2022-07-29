from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import TaskForm
from todoapp.models import Task

def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        todo = Task(name=name, priority=priority,date=date)
        todo.save()
    return render(request,'home.html',{'task1': task1})

# def details(request):
#     todo = Task.objects.all()
#     return render(request,'home.html',{'task' : todo})

def update(request,id):
    task_id = Task.objects.get(id=id)
    form = TaskForm(request.POST or None,instance=task_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form' : form,'task' : task_id})


def delete(request,id):
    task_id=Task.objects.get(id=id)
    if request.method=='POST':
        task_id.delete()
        return redirect('/')
    return render(request,'delete.html')