

 #Create a new Django project and call it: Project_two
 #Create a new Django App and call it: AppTwo
 #Create an index view that returns: <em>My Second App</em>
 #Link this view to the urls.py file

from django.shortcuts import render
from django.http import HttpResponse

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def index(request):
    return HttpResponse("<em> Wecome to the Index page of Django </em>")

def help(request):
    my_dict={'insert_me':'This is your Help Page !'}
    return render(request,'help.html',context=my_dict)

