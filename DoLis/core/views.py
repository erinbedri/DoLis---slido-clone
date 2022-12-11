from django.shortcuts import render

from DoLis.core.models import Event


def homepage(request):
    events = Event.objects.all()
    events_count = events.count()

    context = {
        'events': events,
        'events_count': events_count,
    }

    return render(request, 'core/homepage.html', context)

