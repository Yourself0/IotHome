from django.db import models
from django.contrib.auth.models import User

class DeviceState(models.Model):
    device_id = models.CharField(max_length=100)  # or whatever field type you need
    button_number = models.IntegerField()
    device_name = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=10)  # Assuming states are "On" or "Off"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return f"{self.device_name} (ID: {self.device_id}) - Button {self.button_number}: {self.state}"

    # Optionally override save method to set additional fields or perform actions
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method

# Example function to query DeviceState using username
def get_device_states_by_username(username):
    try:
        devices = DeviceState.objects.filter(user__username=username)
        return devices
    except User.DoesNotExist:
        return []  # Return an empty list if the user doesn't exist
