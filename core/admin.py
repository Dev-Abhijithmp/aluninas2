from django.contrib import admin
from .models import Userprofile,Job,Event

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Job)
admin.site.register(Event)