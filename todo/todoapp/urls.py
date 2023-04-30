from django.urls import path
from .views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete, home
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', TodoList.as_view(), name='todo-list'),
    path('create', TodoCreate.as_view(), name='todo-create'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='todo-detail'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='todo-update'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='todo-delete'),
]
