from django.core.cache import cache
from django.db import IntegrityError
from rest_framework import serializers
from event_app.models.event_tables import Event
from event_app.models.attendee_tables import Attendee


class RegisterationSerializer(serializers.Serializer):
    event = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_event(self, value):
        event_id = self.context.get("event_id")
        try:
            event = Event.objects.get(id=event_id)
            if event.is_full:
                raise serializers.ValidationError("Event is full.")
        except Event.DoesNotExist:
            raise serializers.ValidationError("Event not found.")

        return event

    def validate_email(self, value):
        event_id = self.context.get("event_id")
        value = value.lower()
        if not self._validate_with_cache(event_id, value):
            self._validate_with_db(event_id, value)
        return value

    def _validate_with_cache(self, event_id, email):
        cache_key = f"event_{event_id}_emails"
        cached_emails = cache.get(cache_key)
        if cached_emails is not None:
            if email in cached_emails:
                raise serializers.ValidationError(
                    "You are already registered for this event."
                )

    def _validate_with_db(self, event_id, email):
        emails = set(
            Attendee.objects.filter(event__id=event_id).values_list("email", flat=True)
        )
        if email in emails:
            cache_key = f"event_{event_id}_emails"
            cache.set(cache_key, emails, timeout=None)
            raise serializers.ValidationError(
                "You are already registered for this event."
            )

    def create(self, validated_data):
        try:
            return Attendee.objects.create(**validated_data)
        except IntegrityError:
            """ for fallback support"""
            raise serializers.ValidationError(
                {"email": ["You are already registered for this event."]}
            )
