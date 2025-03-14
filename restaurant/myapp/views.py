# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def booking(request):
    return render(request, 'booking.html')

def event(request):
    return render(request, 'event.html')

def food(request):
    return render(request, 'food.html')

def gall(request):
    return render(request, 'gall.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def key(request):
    return render(request, 'key.html')

def ar(request):
    return render(request, 'ar.html')

def login(request):
    return render(request, 'login.html')

def login(requests):
    if requests.method=='POST':
        username=requests.POST['username']
        password=requests.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(requests,user)
            return redirect('/')
        else:
            messages.info(requests,'invalid credentials')
    else:
        return render(requests,'login.html')

def register(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        return redirect('login')
    else:
        return render(request,'reg.html')



    
def logout(request):
    auth.logout(request)
    return redirect('/')


