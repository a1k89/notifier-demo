import uuid

from django.db import models
from django.contrib.auth import get_user_model

from ..conf import \
    ClientAction, \
    Icon

from .managers import NotificationManager


class Notification(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,
                           editable=True,
                           unique=True)
    name = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    recipients = models.ManyToManyField(get_user_model())
    is_notify_screen = models.BooleanField(default=True)
    is_push = models.BooleanField(default=True)
    client_action = models.CharField(choices=ClientAction.choices,
                                     default=ClientAction.NONE,
                                     max_length=250)

    icon = models.CharField(blank=True,
                            max_length=250,
                            choices=Icon.choices,
                            default=Icon.INFO)
    objects = models.Manager()
    actions = NotificationManager()
