from django.db.models.signals import post_save  #this is th signal that get fired after the user is saved
from django.contrib.auth.models import User #this user model is what we call the sender, it sends the signal
from django.dispatch import receiver #
from .models import Profile

@receiver(post_save, sender=User)# When a user is saved then send this signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)# When a user is saved then send this signal
def save_profile(sender, instance, **kwargs):
    instance.profile.save()