from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('date', 'name', 'location', 'slug',
                  'facilitator', 'level', 'description', 'image',)


