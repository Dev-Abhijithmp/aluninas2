from ast import For
import email
from unicodedata import name
from django.shortcuts import render
from django.core import serializers
import json

# Create your views here.
from .models import  Participants, Userprofile,Job,Event,Participants
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_authenticated:
        print('user')
        print(request.user.is_staff)
        return redirect('home')
    else:
        events = Event.objects.all()
        context={
            'event':events
        }
        return render(request,'index.html',context)
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
                data = Userprofile.objects.get(email=request.user.username)
                print('username')
                print(user.is_staff)
                print(request.user.username)
              
                if data.verified==True:
                    if user.is_staff:
                        return redirect('staffhome')
                    else: 
                        return redirect('home')
                else:
                    return redirect('verification')
                
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
        role =request.POST['role']
        if pass1 == "" or pass2 == ""or email == "" or email ==""or gender == "" or name =='' :
            messages.info(request, 'please fill all the fields')
            return render(request, 'registration.html')
        else:
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return render(request, 'registration.html')
                else:

                    user = User.objects.create_user(
                        username=email, password=pass1, email=email)
                    user.save()
                    usern = auth.authenticate(username=email, password=pass1)
                    auth.login(request, usern)
                    profile =Userprofile.objects.create(name=name,email=email,phone=phone,gender=gender,dob=dob,course=course,role=role)
                    return redirect('verification')
            else:
                messages.info(request, 'Password not matching')
                return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')        
@login_required(login_url='login')
def home(request):
    data = Userprofile.objects.get(email=request.user.username)
    context={
        'data':data,   
    }
    return render(request,'home.html',context)

def staffhome(request):
    data = Userprofile.objects.get(email=request.user.username)
    users = Userprofile.objects.filter(is_staff=False,is_superuser=False,verified=False,rejected=False,)
    context={
        'data':data,
        'users':users
    }
    return render(request,'staff/staffhome.html',context)
def acceptuser(request,):
    val =request.GET['email']
    print(val)
    data = Userprofile.objects.get(email=val)
    data.verified=True
    data.save()
    return redirect('staffhome')
def rejectuser(request):
    val =request.GET['email']
    print(val)
    data = Userprofile.objects.get(email=val)
    data.rejected=True
    data.save()
    return redirect('staffhome')
def deletejob(request):
    val =request.GET['id']
    print(val)
    data = Job.objects.get(id=val)
    data.delete()
    
    return redirect('staffjob')
def deleteevent(request):
    val =request.GET['id']
    print(val)
    data = Event.objects.get(id=val)
    data.delete()
    return redirect('staffevent')
@login_required(login_url='login')
def job(request):
    job=Job.objects.all()
    context={
        'job':job
    }
    return render(request,'job.html',context)
@login_required(login_url='login')
def staffjob(request):
    job=Job.objects.all()
    context={
        'job':job
    }
    
    return render(request,'staff/staffjob.html',context)
@login_required(login_url='login')
def staffcreatejob(request):
    if request.method == 'POST':
        jobpost = request.POST['jobname']
        jobdesc =request.POST['jobdescription']
        Job.objects.create(jobdesc=jobdesc,jobpost=jobpost)
        return redirect('staffjob')

    return render(request,'staff/staffcreatejob.html')

@login_required(login_url='login')
def createjob(request):
    if request.method == 'POST':
        jobpost = request.POST['jobname']
        jobdesc =request.POST['jobdescription']
        Job.objects.create(jobdesc=jobdesc,jobpost=jobpost)
    
        return redirect('job')
@login_required(login_url='login')
def profile(request):
    data = Userprofile.objects.get(email=request.user.username)
    context={
        'data':data
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def staffprofile(request):
    data = Userprofile.objects.get(email=request.user.username)
    context={
        'data':data
    }
    return render(request,'staff/staffprofile.html',context)
def staffevent(request):
    event = Event.objects.all()
    context= {
        'event':event
    }
    return render(request,'staff/staffevent.html',context)
@login_required(login_url='login')
def staffeventcreate(request):
    if request.method=='POST':
        name =request.POST.get('eventname')
        date =request.POST.get('eventdate')
        venue =request.POST.get('eventvenue')
        time =request.POST.get('eventtime')
        role =request.POST.get('role')
        ob=Event.objects.create(name=name,venue=venue,date=date,eventtime=time,role=role)
        return redirect('staffevent')
    return render(request,'staff/staffeventcreate.html')
def event(request):
    if request.method=='POST':
        name =request.POST.get('name')
        venue =request.POST.get('venue')
        date =request.POST.get('date')
        time =request.POST.get('time')
        ids =request.POST.get('id')
        Participants.objects.create(name=name,venue=venue,date=date,eventtime=time,eventid=ids,email=request.user.username)
        event = Event.objects.all()
        

        context= {
            'event':event
        }
        return render(request,'event.html',context)
    else:
        udata =Userprofile.objects.get(email=request.user.username)
        event = Event.objects.all()
        if udata.role == 'ALUMNI':
            event = Event.objects.filter(role ='ALL')
            print(udata.role)
        
        obj =Participants.objects.filter(email=request.user.username)
        print(obj)
        tmpjson = serializers.serialize('json', obj)
        m = json.loads(tmpjson)
        print(m)
        
        if obj.exists():
            v ={}
            for i in event:
                flag =0
                for j in m:

                    if str(i.id) ==j['fields']['eventid']:
                        print(j['fields']['eventid'])
                        flag =1
                if flag == 1:
                    v[i.id]='Applied'
                else:
                    v[i.id]='Notapplied'

            print(v)       
            context= {
            'event':event,
            'data':v,
            }
            return render(request,'event.html',context)
            
        else:
            context= {
            'event':event,
            'data':'null',
            }
            return render(request,'event.html',context)
            

        
        
def participants(request):
    p = Participants.objects.all()
    context= {
        'participants':p
    }
    return render(request,'staff/participant.html',context)
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
@login_required(login_url='login')
def verification(request):
    return render(request, 'verificationpage.html')
def applyevent(request):
    ids=request.GET['id']
    ev = Event.objects.get(id=ids)
    Participants.objects.create(email=request.user.username,name=str(ev.name),eventid=ids,date=str(ev.date),venue=str(ev.venue),eventtime=str(ev.eventtime))
    return redirect('event')

