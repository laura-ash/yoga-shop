from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
import sweetify


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Message successfully sent',
                position='top-right', toast='true', icon='success',
                    timer='3000',)
            return redirect('contact')
        else:
            sweetify.success(request, 'Unsuccessful. Please check each
                form field is valid!', position='top-right', toast='true',
                    icon='success', timer='3000',)
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

    return render(request, 'contact/submissions.html',
    {'submissions': submissions})


def update_submission(request, pk):
    submission = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Successfully updated.',
            position='top-right', toast='true', icon='success', timer='3000',)
        else:
            sweetify.success(request, 'Update unsuccessful. Please check all fields
            are valid and try again.', position='top-right', toast='true', icon='error', timer='3000',)
    return redirect(submissions)


def delete_submission(request, pk):
    submission = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        submission.delete()
        sweetify.success(request, 'Successfully deleted.', position='top-right',
        toast='true', icon='success', timer='3000',)
    else:
        sweetify.success(request, 'Deletion unsuccessful. Please try again.',
        position='top-right', toast='true', icon='error', timer='3000',)
    return redirect(submissions)
