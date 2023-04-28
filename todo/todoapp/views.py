from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
# Create your views here.

def home(request):
    return render(request, 'home.html')


class TodoCreate(CreateView):
    model = Todo.objects.all()
    fields = '__all__'

class TodoList(ListView):
    model = Todo.objects.all()
    #template_name = 'todo.html'
    #context_object_name = 'todos'

class TodoDetail(DetailView):
    model = Todo.objects.all()
    #template_name = 'todo.html'
    context_object_name = 'todo'

class TodoUpdate(UpdateView):
    model = Todo.objects.all()
    fields = '__all__'
    #template_name = 'todo.html'
    context_object_name = 'todo'

class TodoDelete(DeleteView):
    model = Todo.objects.all()
    #template_name = 'todo.html'
    context_object_name = 'todo'


