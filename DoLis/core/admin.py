from django.contrib import admin

from DoLis.core.models import Event, Question


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'event')