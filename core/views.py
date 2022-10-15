from django.shortcuts import render

# Create your views here.
from .models import  Userprofile
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    print(request.user)
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        print(email), print(password)
        if email  == "" or password =="":
            messages.info(request, "please fill all the fields")
            return redirect('login')
        else:
            user = auth.authenticate(username=email, password=password)
            
            print(user)
            if user is not None:
                auth.login(request, user)
                print(request.user)

                return redirect('home')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'login.html')

    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['repass']
        phone =request.POST['phone']
        name =request.POST['name']
        dob =request.POST['dob']
        course =request.POST['course']
        gender =request.POST['gender']
        if pass1 == "" or pass2 == ""or email == "":
            messages.info(request, 'please fill all the fields')
            return redirect('register')
        else:
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('register')
                else:

                    user = User.objects.create_user(
                        username=email, password=pass1, email=email)
                    user.save()
                    usern = auth.authenticate(username=email, password=pass1)
                    auth.login(request, usern)
                    profile =Userprofile.objects.create(name=name,email=email,phone=phone,gender=gender,dob=dob,course=course)
                    return redirect('home')
            else:
                messages.info(request, 'Password not matching')
                return redirect('register')

    else:
        return render(request, 'registration.html')        
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def staffhome(request):
    return render(request,'staffhome.html')
@login_required(login_url='login')
def job(request):
    return render(request,'job.html')
def createjob(request):
    return render(request,'createjob.html')
def profile(request):
    return render(request,'profile.html')

def event(request):
    return render(request,'event.html')
def createevent(request):
    return render(request,'createevent.html')
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
