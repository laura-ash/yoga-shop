from django.shortcuts import render, redirect, get_object_or_404
from django. contrib import messages
from .forms import EventForm
from .models import Event

import sweetify


def events(request):
    events = Event.objects.all().order_by('date')

    return render(request, 'events/events.html', {'events': events})


def event_space(request):
    return render(request, 'events/event-space.html')


def create_event(request):
    event_form = EventForm()
    context = {
            'event_form': event_form,
        }

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event_form.save()
            sweetify.success(request, 'Event created successfully.', position='top-right', toast='true',
            icon='success', timer= '3000',)
            return redirect('events')
        else:
            event_form = EventForm()
            sweetify.success(request, 'Event creation unsuccessful. Please ensure all fields are valid and try again',
            position='top-right', toast='true', icon='error', timer= '3000',)
            template = 'events/create-event.html'
        
    return render(request, 'events/create-event.html', context)


def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event_form = EventForm(request.POST, request.FILES, instance=event)
        if event_form.is_valid():
            event_form.save()
            sweetify.success(request, 'Event updated successfully.', position='top-right', toast='true',
            icon='success', timer= '3000',)
        else:
            print('form not valid')
            print(event_form)
            sweetify.success(request, 'Event update unsuccessful. Please ensure all fields are valid and try again.',
                position='top-right', toast='true', icon='error', timer= '3000',)
    return redirect(events)


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        sweetify.success(request, 'Event deleted successfully.', position='top-right', toast='true',
            icon='success', timer= '3000',)
    else: 
        sweetify.success(request, 'Event deletion unsuccessful. Please try again.',
            position='top-right', toast='true', icon='error', timer= '3000',)
    return redirect(events)
