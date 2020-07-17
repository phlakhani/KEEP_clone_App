from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import Task_form
# Create your views here.


def index(request):
    alltasks = Task.objects.all()
    form = Task_form()

    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            form.save()
    form = Task_form()  # to keep form input empty after submitting
    context = {
        "tasks": alltasks,
        "form": form
    }
    return render(request, 'list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = Task_form(instance=task)

    if request.method == 'POST':
        form = Task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")  # redirect page to home page after update
    context = {
        "form": form
    }

    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    tsk = Task.objects.get(id=pk)

    if request.method == 'POST':
        tsk.delete()
        return redirect("/")  # redirect page to home page after delete

    context = {
        "task": tsk
    }
    return render(request, 'delete_confirm.html', context)
