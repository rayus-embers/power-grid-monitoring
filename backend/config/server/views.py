from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TargetSerializer, Values30minSerializer, LogsSerializer
from .models import Target, Values30min, Logs
from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from datetime import datetime, timedelta
# Create your views here.
class TargetAPIView(generics.ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

class FilterValuesView(generics.ListAPIView):
    serializer_class = Values30minSerializer

    def get_queryset(self):
        device = self.request.query_params.get('device')
        dev_typ = self.request.query_params.get('dev_typ')
        substation = self.request.query_params.get('substation')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        days = self.request.query_params.get('days')
        if days:
            try:
                end_date = datetime.now()
                start_date = end_date - timedelta(days=int(days))
            except ValueError:
                return []
        else:
            try:
                start_date = parse_datetime(start_date)
                end_date = parse_datetime(end_date)
            except ValueError:
                return []

        return Values30min.objects.filter(
            device__dev=device,
            device__susbstation=substation,
            device__dev_typ=dev_typ,
            time__range=(start_date, end_date)
        ).order_by('time')
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"error": "No data found for the provided filters."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FilterLogsView(generics.ListAPIView):
    serializer_class = LogsSerializer
    #you can filter based on days or just give the start date and end date
    def get_queryset(self):
        device = self.request.query_params.get('device')
        dev_typ = self.request.query_params.get('dev_typ')
        substation = self.request.query_params.get('substation')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        days = self.request.query_params.get('days')
        if days:
            try:
                end_date = datetime.now()
                start_date = end_date - timedelta(days=int(days))
            except ValueError:
                return []
        else:
            try:
                start_date = parse_datetime(start_date)
                end_date = parse_datetime(end_date)
            except ValueError:
                return []
        return Logs.objects.filter(
            device__dev=device,
            device__susbstation=substation,
            device__dev_typ=dev_typ,
            time__range=(start_date, end_date)
        ).order_by('time')
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"error": "No logs found for the provided filters."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)