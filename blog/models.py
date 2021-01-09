from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.CharField(max_length=140, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Return title of post
    def __str__(self):
        return self.title

    def intro(self):
        return self.body[:60] + '...'