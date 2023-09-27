from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    """Abstract base model with self-updating `created_at` and `updated_at` fields."""
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated')

    class Meta:
        abstract = True


class CustomUser(AbstractUser, TimeStampedModel):
    pass
