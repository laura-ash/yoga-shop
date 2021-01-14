from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def contact(request):

    contact_form = ContactForm()

    template = 'contact/contact_us.html'
    context = {
        'contact_form': contact_form,

}

    return render(request, 'contact/contact_us.html', context)

