from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    facilitator = models.CharField(max_length=140, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)



    def __str__(self):
        if self.name:
            return self.name
