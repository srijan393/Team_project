# monitoring/models.py

from django.db import models

class AirQualityData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Temp: {self.temperature}°C, Humidity: {self.humidity}%, AQ: {self.air_quality}"
