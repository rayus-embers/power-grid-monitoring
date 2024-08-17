from django.urls import path
from .views import TargetAPIView, FilterValuesView, FilterLogsView

urlpatterns = [
    path('', TargetAPIView.as_view(), name='view-target'),
    path('values/', FilterValuesView.as_view(), name='filter-values'),
    path('logs/', FilterLogsView.as_view(), name='filter-logs'),
]
