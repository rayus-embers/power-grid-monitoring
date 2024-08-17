from rest_framework import serializers
from .models import Target, Values30min, Logs

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class Values30minSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source='device.unit')
    class Meta:
        model = Values30min
        fields = ['time', 'value', 'device', 'unit']

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['time', 'title', 'description', 'danger', 'device']