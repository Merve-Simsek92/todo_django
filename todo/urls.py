from django.urls import path
from .views import todo_add,index,todo_update,todo_delete,todo_detail

urlpatterns = [
   
    path("",index, name="home"),
    path("add/",todo_add,name="add",),
    path("update/<int:id>",todo_update,name="update"),
    path('delete/<int:id>',todo_delete,name='delete'),
    path('todo/<int:id>', todo_detail, name="detail"),
 
]