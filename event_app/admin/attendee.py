from django.contrib import admin
from event_app.models import Attendee

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    """Admin View for Consumer Profile"""

    list_display = (
        "event__id",
        "name",
        "email",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "email")
    readonly_fields = ("created_at", "updated_at")