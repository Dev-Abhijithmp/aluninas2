from django.db import models

# Create your models here.
class Userprofile(models.Model):
    email =models.TextField()
    name =models.TextField()
    dob =models.DateField()
    gender =models.TextField()
    phone =models.TextField()
    course = models.TextField()
    role=models.TextField(default="STUDENT")
    verified=models.BooleanField(default=False)
    def __str__(self):
        return self.email