from django.shortcuts import render
from user_app.models import User

# Create your views here.
def index(request):
    return render(request,'user_app/index.html')

def user(request):
    users_list = User.objects.all() # get all the users
    return render(request, 'user_app/user.html', {'user': users_list})
    
