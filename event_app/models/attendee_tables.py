from django.db import models
from .event_tables import Event
from .base_table import TimestampedModel
# Create your models here.
class Attendee(TimestampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registered_events')
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        unique_together = ('event', 'email')

    def __str__(self):
        return f"{self.name} - {self.email}"