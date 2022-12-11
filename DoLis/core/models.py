from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Event(models.Model):
    owner = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )

    name = models.CharField(
        max_length=255,
    )

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    description = models.TextField(
        max_length=1500,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'Event Name: {self.name}'


class Question(models.Model):
    author = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )

    event = models.ForeignKey(
        Event,
        on_delete=CASCADE,
    )

    body = models.TextField(
        max_length=1500,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    parent = models.ForeignKey(
        'self',
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    def __str__(self):
        return f'{self.body} - {self.author}'