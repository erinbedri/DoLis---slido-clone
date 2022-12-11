from django.contrib import admin

from DoLis.core.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
