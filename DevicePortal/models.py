from django.db import models
from django.contrib.auth.models import User  # Import the User model

class DeviceRegistered(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=100, unique=True, verbose_name='Device ID')
    device_name = models.CharField(max_length=100, verbose_name='Device Name')
    device_type = models.CharField(max_length=100, verbose_name='Device Type')
    user_id = models.IntegerField(verbose_name='User ID')  # Store user ID manually
    username = models.CharField(max_length=150, verbose_name='Username', null=True, blank=True)  # Ensure this is a CharField

    class Meta:
        db_table = 'DevicePortal_deviceregistered'
        ordering = ['id']

    def __str__(self):
        return f"{self.device_name} ({self.device_id})"