from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from board.models import Profile, Employer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    # if not created:
    #     Profile.objects.create(user=instance)
    instance.profile.save()

# Employer Profile creation signals
@receiver(post_save, sender=User)
def create_employer(sender, instance, created, **kwargs):
    if created:
        Employer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_employer(sender, instance, **kwargs):
    instance.employer.save()

