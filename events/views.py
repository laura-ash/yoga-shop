from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event

def events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_space(request):
    return render(request, 'events/event-space.html')

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
    return redirect(events)
