from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event


def events(request):
    events = Event.objects.all().order_by('date')

    return render(request, 'events/events.html', {'events': events})


def event_space(request):
   return render(request, 'events/event-space.html')


def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        context = {
            'event_form': event_form,
        }

        if event_form.is_valid():
            event_form.save()
            return redirect('events')
    else:
        
        event_form = EventForm()

        template = 'events/create-event.html'
        context = {
            'event_form': event_form,
        }

    return render(request, 'events/create-event.html', context)


def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
    return redirect(events)

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
    return redirect(events)