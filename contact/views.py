from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:

        contact_form = ContactForm()

        template = 'contact/contact-us.html'
        context = {
            'contact_form': contact_form,

        }

    return render(request, 'contact/contact-us.html', context)

def submissions(request):
    submissions = Contact.objects.all().order_by('date')
    form = ContactForm()
    context = {'form': form}

    return render(request, 'contact/submissions.html', {'submissions': submissions})


def update_submission(request, pk):
    submission = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
    return redirect(submissions)
