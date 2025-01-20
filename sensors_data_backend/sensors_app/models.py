from django.db import models

class SensorData(models.Model):
    date = models.DateTimeField()
    acc_x = models.FloatField()
    acc_y = models.FloatField()
    acc_z = models.FloatField()
    gyro_x = models.FloatField()
    gyro_y = models.FloatField()
    gyro_z = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    activity_name = models.CharField(max_length=255)
    behaviour_name = models.CharField(max_length=255)
    custom_event = models.CharField(max_length=255)