from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, RegistrationForm, RegisterUserForm


def home(request):
    return render(request, 'events/home.html')


def events_list(request):
    
    events = Event.objects.all().order_by('event_date')
    return render(request, 'events/events_list.html', {'events': events})


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            return render(request, 'events/registration_success.html', {
                'event': event,
                'registration': registration,
            })
    else:
        form = RegistrationForm()
    return render(request, 'events/register_event.html', {
        'form': form,
        'event': event,
    })


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'events/register.html', {'form': form})