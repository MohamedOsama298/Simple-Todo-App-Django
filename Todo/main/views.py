from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import TodoForm, TodoItemsForm,UserCreation
from .models import Todo
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    user = request.user
    todos = Todo.objects.filter(user=user)
    form = UserCreation()
    context = {
        "todos" : todos,
    }
    return render(request,"home.html",context)

def detailed(request , id):
    todo = Todo.objects.get(id = id)
    items = todo.todoitems_set.all()
    context={
        "todo": todo,
        "items" :items
    }
    return render(request , 'detaild.html' , context)




def createTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'create.html' , context)

def updateTodo(request , pk):
    todo = Todo.objects.get(id= pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'update.html' , context)



def delete(request , pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def createTodoItem(request,id):
    form = TodoItemsForm()
    if request.method == 'POST':
        form =  TodoItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "itemform": form,
    }
    return render(request, 'createItemTodo.html',context)

def updateTodoItem(request, pk):
    todoItem = TodoItems.objects.get(id=pk)
    form= TodoItemsForm(instance=todoItem)
    if request.method == 'POST':
        form = TodoItemsForm(request.POST, instance=todoItem)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'components/updateItem.html', context)

def deleteTodoItem(request, pk):
    todoItem = TodoItems.objects.get(id=pk)
    todoItem.delete()
    return redirect('/')



def CreateUser(request):
    form = UserCreation()
    if request.method == 'POST':
        form=UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    
    return render(request,'signup.html',context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request ,user)
            print (user)
            return redirect('/')
    context = {
        
    }
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')