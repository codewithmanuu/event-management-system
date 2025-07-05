from django.urls import path
from event_app.views import event_register
from event_app.views import attendee_register
urlpatterns = [
    path("events/", event_register.HostEventAPI.as_view(), name="host_event"),
    path("events/<str:event_id>/register/", attendee_register.EventRegisterAPI.as_view(), name="event_register"),
    path("events/<str:event_id>/attendees/", attendee_register.FetchAttendeesAPI.as_view(), name="event_attendees"),
]
