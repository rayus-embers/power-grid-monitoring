from django.db import models


units = [
    ("MW", "MW"),
    ("KV", "KV"),
    ("Hz", "Hz"),
]
dangers = [
    ("Casual", "Casual"),
    ("Warning","Warning"),
    ("Dangerous","Dangerous"),
]
# Create your models here.
class Target(models.Model):
    susbstation = models.CharField(max_length=50)
    dev_typ = models.CharField(max_length=50)
    dev = models.CharField(max_length=50)
    unit = models.CharField(choices=units, max_length=3)
    def __str__(self):
        return self.dev + ":" + self.unit
    

class Values30min(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()
    device = models.ForeignKey(Target, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.device.dev} at {self.time} is {self.value}{self.device.unit}"

class Logs(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    danger = models.CharField(max_length=10, choices=dangers)
    device = models.ForeignKey(Target, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} in {self.device.susbstation} to {self.device.dev_typ}; {self.device.dev} at {self.time}"
    