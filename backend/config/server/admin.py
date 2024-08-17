from django.contrib import admin
from .models import Target, Values30min, Logs
# Register your models here.
admin.site.register(Target)
admin.site.register(Values30min)
admin.site.register(Logs)