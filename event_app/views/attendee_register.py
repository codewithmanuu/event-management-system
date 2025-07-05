from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from event_app.models.attendee_tables import Attendee
from rest_framework.pagination import PageNumberPagination
from event_app.serializers.attendee_serializers import RegisterationSerializer


class EventRegisterAPI(APIView):
    @extend_schema(request=RegisterationSerializer,responses={201: None, 400: dict})
    def post(self, request, event_id):
        data = request.data.copy()
        data["event"] = event_id
        serializer = RegisterationSerializer(data=data, context={"event_id": event_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchAttendeesAPI(APIView):
    def get(self, request, event_id):
        attendees = Attendee.objects.filter(event=event_id)
        paginator = PageNumberPagination()
        paginated_attendees = paginator.paginate_queryset(attendees, request)
        serializer = RegisterationSerializer(paginated_attendees, many=True)
        return paginator.get_paginated_response(serializer.data)
