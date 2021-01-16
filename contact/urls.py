from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('submissions', views.submissions, name='submissions')
]