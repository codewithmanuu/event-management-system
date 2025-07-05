import uuid
from django.db import models
from .base_table import TimestampedModel
from django.core.validators import MinValueValidator
# Create your models here.

class Event(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    @property
    def is_full(self):
        return self.registered_events.count() >= self.max_capacity