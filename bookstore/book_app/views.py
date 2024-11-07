from django.shortcuts import render, get_object_or_404
from book_app import forms
from book_app.models import BookInfo ,Category

# Create your views here.

#def index(request):
  #  return render(request,'book_app/index.html')

def Category_list(request):
    categories = Category.objects.all()
    return render(request,'book_app/category_list.html', {'categories': categories})


def BookViews(request):
    books = BookInfo.objects.all() # get all the users
    return render(request,'book_app/book_list.html',{'books':books})
    

def BookDetails(request,id):
    book = get_object_or_404(BookInfo,id=id)
    return render(request,'book_app/bookdetails.html',{'book':book})
    #books = BookInfo.objects.get(id=id)
    #context = {'book':books,}
    #return render(request,'bookdetails.html',context)
