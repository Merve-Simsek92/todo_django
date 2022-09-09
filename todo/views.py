from django.shortcuts import render,redirect
from .forms import  TodoForm
from .models import Todo

# Create your views here.

def index(request):
    todos=Todo.objects.all()
    context={
        "todos":todos
    }
    return render(request, 'todo/home.html',context)


def todo_add(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        'form': form
    }

    return render(request, 'todo/todo_add.html', context)

def todo_update(request,id ):
    todo=Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={
        'form':form
    }
    return render(request,'todo/todo_update.html',context)


def todo_delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("home")
    context={
        "todo":todo
    }  
    return render(request,"todo/todo_delete.html",context)  

def todo_detail(request, id):        
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_detail.html', context)