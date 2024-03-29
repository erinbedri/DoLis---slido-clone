from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from DoLis.core.forms import QuestionForm, LoginForm, RegistrationForm, EventCreateForm, EventEditForm
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
    recent_questions = Question.objects\
        .filter(event=event)\
        .order_by('-created_at')
    oldest_questions = Question.objects\
        .filter(event=event)\
        .order_by('created_at')
    questions_count = len([q for q in recent_questions if not q.parent])

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_obj = Question.objects.get(id=parent_id)
                if parent_obj:
                    reply_question = form.save(commit=False)
                    reply_question.author = request.user
                    reply_question.event = event
                    reply_question.parent = parent_obj
                    reply_question.save()
                    return HttpResponseRedirect(reverse('core:event details', args=[str(pk)]))

            question = form.save(commit=False)
            question.event = event
            question.author = request.user
            question.save()
            return HttpResponseRedirect(reverse('core:event details', args=[str(pk)]))
    else:
        form = QuestionForm()

    context = {
        'event': event,
        'recent_questions': recent_questions,
        'oldest_questions': oldest_questions,
        'questions_count': questions_count,
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


@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if question.author == request.user:
        question.delete()

    return redirect('core:event details', question.event.id)


@login_required
def own_events_list(request):
    events = Event.objects.filter(owner=request.user)

    context = {
        'events': events,
    }
    return render(request, 'core/events-own.html', context)


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.owner == request.user:
        event.delete()

    return redirect('core:own events list')


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.owner == request.user:
        if request.method == 'POST':
            form = EventEditForm(request.POST, instance=event)
            if form.is_valid():
                event.save()
                return redirect('core:own events list')
        else:
            form = EventEditForm(instance=event)

        context = {
            'form': form,
        }

        return render(request, 'core/event-edit.html', context)
