from rest_framework import serializers
from apps.api.models import Event, Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attendance
        fields = ['id', 'owner', 'event', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attendances = AttendanceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'owner', 'name', 'type', 'date', 'time',
                  'price', 'address', 'attendances', 'created_at', 'updated_at']

