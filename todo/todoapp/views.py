from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

class TodoList(ListView):
    model = Todo
    template_name = 'todo.html'
    context_object_name = 'todo'

    def get_queryset(self):
        """Return a QuerySet containing all Todo objects."""    
        return Todo.objects.all()

class TodoCreate(CreateView):
    model = Todo.objects.all()
    form_class=TodoForm
    template_name = 'todo_create.html'
    success_url = '/todo/list/'   

class TodoDetail(DetailView):
    model = Todo.objects.all()
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

    def get_queryset(self):
        """Return a QuerySet containing all Todo objects."""
        return Todo.objects.all()
    
    

class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo_create.html'
    success_url = reverse_lazy('/todo/list/')
    
    def get_queryset(self):
        """Return a QuerySet containing all Todo objects."""
        return Todo.objects.all()


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('/todo/list/')

    def get_queryset(self):
        """Return a QuerySet containing all Todo objects."""
        return Todo.objects.all()
    

