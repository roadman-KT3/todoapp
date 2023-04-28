from django.urls import path
from .views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete, home
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', TodoList.as_view(), name='todo-list'),
    path('create', TodoCreate.as_view(), name='todo-create'),
    path('<int:pk>', TodoDetail.as_view(), name='todo-detail'),
    path('<int:pk>/update', TodoUpdate.as_view(), name='todo-update'),
    path('<int:pk>/delete', TodoDelete.as_view(), name='todo-delete'),
]
