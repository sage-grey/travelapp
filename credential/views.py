from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    return render(request,'login.html')

def signup(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']



        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                print("username is taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                print("email is taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')


    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')





# Create your views here.
