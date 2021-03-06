from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('event-space', views.event_space, name='event_space'),
    path('update_event/<int:pk>', views.update_event, name='update_event'),
    path('create-event/', views.create_event, name='create_event'),
    path('delete_event/<int:pk>', views.delete_event, name='delete_event'),
]
