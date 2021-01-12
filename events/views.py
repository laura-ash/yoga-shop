from django.shortcuts import render
from .models import Event

def events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_space(request):
    return render(request, 'events/event-space.html')