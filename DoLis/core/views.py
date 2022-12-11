from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from DoLis.core.models import Event, Question


def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    events = Event.objects.filter(Q(code__icontains=q))
    events_count = events.count()

    context = {
        'events': events,
        'events_count': events_count,
        'query': q,
    }

    return render(request, 'core/homepage.html', context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    questions = Question.objects\
        .filter(event=event)\
        .order_by('-created_at')

    context = {
        'event': event,
        'questions': questions,
    }

    return render(request, 'core/event-details.html', context)