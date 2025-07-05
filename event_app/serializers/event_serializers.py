from django.utils import timezone
from rest_framework import serializers
from event_app.models.event_tables import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def validate(self, data):
        if data["start_time"] < timezone.now():
            raise serializers.ValidationError(
                {"start_time": "Start time must be in the future."}
            )
        if data["end_time"] <= data["start_time"]:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time."}
            )
        return data
