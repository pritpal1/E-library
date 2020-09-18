from django.contrib import admin
from Book import views
from django.urls import path
urlpatterns = [
    #path("",views.index,name="index"),
    path('',views.listView,name="listView"),
    path('detail/<int:id>',views.Detailview,name="DetailView"),
    path('create',views.book_create,name="book_create"),
    path('delete/<int:id>',views.delete),
   
]
