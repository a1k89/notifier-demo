import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uid = models.UUIDField(default=uuid.uuid4,
                           editable=True,
                           unique=True)
