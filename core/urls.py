from django import views
from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('job',views.job,name='job'),
    path('createjob',views.createjob,name="createjob"),
    path('profile',views.profile,name='profile'),
    path('event',views.event,name='event'),
    path('logout',views.logout,name='logout'),
    path('verification',views.verification,name='verification'),
    path('staffhome',views.staffhome,name='staffhome'),
    path('staffprofile',views.staffprofile,name='staffprofile'),  
    path('staffeventcreate',views.staffeventcreate,name='staffeventcreate'), 
    path('staffevent',views.staffevent,name='staffevent'), 
    path('staffjob',views.staffjob,name='staffjob'), 
    path('staffcreatejob',views.staffcreatejob,name='staffcreatejob'), 
    path('acceptuser/',views.acceptuser,name='acceptuser/'), 
    path('rejectuser/',views.rejectuser,name='rejectuser/'), 
    path('deletejob/',views.deletejob,name='deletejob/'), 
    path('deleteevent/',views.deleteevent,name='deleteevent/'), 
    

]