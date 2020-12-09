Bugs: 
Problem: When trying to link images in the website, they were not displaying as expected.
Solution: Needed to add "django.template.context_processors.media" under OPTIONS in TEMPLATES in the settings.py file.
