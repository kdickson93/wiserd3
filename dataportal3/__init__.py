# from django.utils import timezone

__author__ = 'lostvisions'

# Connecting to AllAuth Signals
from allauth.account import signals
from django.dispatch import receiver

from models import UserProfile


@receiver(signals.user_signed_up)
def new_user_signup(sender, **kwargs):
    print "signed up a user!!!!"
    # time_now = datetime.datetime.now()
    # time_now = timezone.now()
    lv_user = UserProfile(user=kwargs['user'])
    # lv_user = UserProfile(user=kwargs['user'], sign_up_timestamp=time_now)
    lv_user.save()


@receiver(signals.user_logged_in)
def user_logged_in(sender, **kwargs):
    print 'logged in', kwargs['user']