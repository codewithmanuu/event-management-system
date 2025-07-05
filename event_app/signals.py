from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save
from event_app.models.attendee_tables import Attendee


@receiver(post_save, sender=Attendee)
def update_attendee_cache(sender, instance, created, **kwargs):
    if created:
        event_id = instance.event.id
        cache_key = f"event_{event_id}_emails"
        cached_emails = cache.get(cache_key, set())
        if not isinstance(cached_emails, set):
            cached_emails = set(cached_emails)
        cached_emails.add(instance.email)
        cache.set(cache_key, cached_emails, timeout=None)
