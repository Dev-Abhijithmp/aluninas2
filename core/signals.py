from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def verifystaffadmin(sender, instance, using, **kwargs):
    print(instance.is_staff)
    if instance.is_staff:
        send_mail(
        'verification',
        'Your verification is successful for Aluminas',
        'abhi001122abhi@gmail.com',
        [instance.username],
        fail_silently=False,
        )