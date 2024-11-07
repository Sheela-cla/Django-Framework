from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


@login_required
def special(request):
    return httpresponse("You are logged in, Nice!")
    
@login_required    
def user_logout(request):
    logout(request)
    return httpresponseredirect(reverse('index'))

def register(request):
    registered = False 
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data =request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,'basic_app/registration.html',
                    {'user_form':user_form,'profile_form':profile_form,
                    'registered':registered})
                

def user_login(request):
    if request.method == 'POST':
        #First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        #django built-in authencation function
        user = authenticate(username = username,password = password)
        # if we have users
        if user:
            # check if the account is active
            if user.is_active:
                #log the user in
                login(request,user)
                #send the user back to some page
                #In this case thiser home page
                return httpresponseredirect(reverse('index'))
            else:
                #if account is not active
                return httpresponse("Account not Active")
        else:
            print("Someone tried to login and failed")
            print("username: {} and password {}".format(username,password))
            return httpresponse("Invalid login details supplied!")
    else:
        return render(request,'basic_app/login.html',{})