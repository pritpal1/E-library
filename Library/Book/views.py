from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from .form import BookForm
def index(request):
    return HttpResponse("in view page")

def listView(request):
    #return HttpResponse("<h1>In Book list view</h1>")
    form=Book.objects.all()
    context={ 
        'form':form
        }
    return render(request,"list.html",context)

def Detailview(request,id=None):
    #return HttpResponse("in deatil view")
    qs=Book.objects.get(id=id)
    context={ 
        'book':qs
        }
    return render(request,"detail.html",context)

def book_create(request,id=None):
    form=BookForm(request.POST or None)
    context={'form':form}
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
    context={
        'form' : BookForm
    }
    template="book_create.html"
    return render(request,template,context) 

def delete(request,id):
    form=Book.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect("/List")

def update_book(request, id=None):
    obj=Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=obj)
    context={'obj':obj,'form':form}
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        return HttpResponseRedirect('/detail/{num}'.format(num=obj.id))
    template = "update_book.html"
    return render(request,template,context)

# def delete(request,id=None):
#     form=get_object_or_404(Book,id=id)
#     if request.method=='POST':
#         form.delete()
#         return HttpResponseRedirect("/list")
#     context={'form':form}
#     template="book_delete.html"

#     return render(request,template,context)
# Create your views here.
