from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message',)


    full_name = forms.CharField(label="Username", required=True)


