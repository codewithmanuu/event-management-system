from datetime import datetime
from event_app.models.event_tables import Event
from rest_framework.generics import ListCreateAPIView
from event_app.serializers.event_serializers import EventSerializer


# Create your views here.
class HostEventAPI(ListCreateAPIView):
    queryset = Event.objects.filter(start_time__gt=datetime.now())
    serializer_class = EventSerializer
