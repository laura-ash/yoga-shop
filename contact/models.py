from django.db import models

from django.conf import settings 


class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    # Return name of contact
    def __str__(self):
        return self.full_name

