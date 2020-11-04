from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime
from datetime import date

# Create your models here.
class User(AbstractUser):
    pass

class Project(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users', blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, default='')
    start_date = models.DateField(default = datetime.date.today)
    end_date = models.DateField(default = date(date.today().year, 12, 31))

    class Status(models.TextChoices):
        ACTIVE = 'Active'
        ON_HOLD = 'On Hold'
        COMPLETED = 'Completed'

    status = models.CharField(max_length=20, choices=Status.choices)

    def __str__(self):
        return self.title


