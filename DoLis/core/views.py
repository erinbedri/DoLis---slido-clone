from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from DoLis.core.forms import QuestionForm, LoginForm, RegistrationForm, EventCreateForm
from DoLis.core.models import Event, Question


def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    events = Event.objects\
        .filter(Q(code__icontains=q))\
        .order_by('-created_at')
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

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.event = event
            question.author = request.user
            question.save()
            return HttpResponseRedirect(reverse('core:event details', args=[str(pk)]))
    else:
        form = QuestionForm()

    context = {
        'event': event,
        'questions': questions,
        'form': form,
    }

    return render(request, 'core/event-details.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('core:homepage')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:homepage')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'core/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('core:homepage')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'core/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('core:homepage')


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('core:event details', event.id)
    else:
        form = EventCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'core/event-create.html', context)