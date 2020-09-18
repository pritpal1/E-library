from django.contrib import admin
from django.urls import path ,include
from Book import views
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',include('Book.urls')),
    path('List/',views.listView,name="listView"),
    path('detail/<int:id>',views.Detailview,name="DetailView"),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update_book),
    path('create',views.book_create,name="book_create"),
    
]
