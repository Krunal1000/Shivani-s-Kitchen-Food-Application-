# import the signal
from django.db.models.signals import post_save
# whenever the user object is saved we get the signal so we want to import User model
from django.contrib.auth.models import User
# now we are sending post_save signal we also want to recieve those particular signal and then it will perform some actions and here in this our action is to create a profile of user while registering automatically.
from django.dispatch import receiver
from .models import Profile

# @receiver(post_save,sender=User)
# def build_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()


