from django.db.models import manager
from django.db import models
from django.contrib.auth import get_user_model

from ..conf import Data


class NotificationManager(models.Manager):
    def create_notification(self, context: Data):
        context_dict = context._asdict()
        instance = self.create(**context_dict)  # Create notification firstly
        if instance:
            for recipient in context.recipients:
                instance.recipients.add(recipient)  # Add User to m2m

    def for_user(self, user):
        return self.get_queryset() \
            .filter(recipients=user,
                     is_notify_screen=True)

