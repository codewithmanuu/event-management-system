from django.contrib import admin
from event_app.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin View for Consumer Profile"""

    list_display = (
        "name",
        "location",
        "start_time",
        "end_time",
        "max_capacity",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "location")
    readonly_fields = ("created_at", "updated_at")