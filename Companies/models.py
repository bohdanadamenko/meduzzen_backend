from Quizzes.models import CustomUser, TimeStampedModel

from django.db import models


class Company(TimeStampedModel):
    """Model representing a company with an owner, name, and optional description."""

    name = models.CharField(max_length=255, verbose_name='Company Name')
    description = models.TextField(
        verbose_name='Company Description', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                              related_name='owned_companies', verbose_name='Owner')
    is_visible = models.BooleanField(
        default=True, verbose_name='Visible for all')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
