from django.shortcuts import render, redirect

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.contrib import messages
from .models import DeviceRegistered  # Import your DeviceRegistered model
from django.db import IntegrityError  # Import IntegrityError
from django.contrib.auth.decorators import login_required  # For user authentication


class DeviceSetting(APIView):
    def post(self,request):
        data = request.data
        print(f"Receive Data :{data}")
        # parsed_data = json.loads(data)
        Device_UID = data.get("Device_UID")
        print(f"Device UID: {Device_UID}")
        return Response({'status':'Data received successfully.'},status = status.HTTP_200_OK)
    




DEVICE_NAME = "Default Device Name"  # Replace with your desired static name
DEVICE_TYPE = "7"  # Replace with your desired static type



@login_required
def add_devices(request):
    context = {
        'header':'Add Devices',
        'id':'Id',
        'Device_id':'Device ID',
        'Device_name':'Device Name',
        'Device_type':'Device Type',

    }
    return render(request, 'startbootstrap/tables.html', context)



'''
@login_required
def add_devices(request):
    if request.method == "POST":
        serial_number = request.POST.get('serial_number')
        device_name = request.POST.get('device_name')

        user_id = request.user.id
        username = request.user.username

        try:
            DeviceRegistered.objects.create(
                device_id=serial_number,
                device_name=device_name,
                device_type=serial_number.split('_')[1] if '_' in serial_number else 'Unknown',
                user_id=user_id,
                username=username  # Ensure this is just a string
            )
            messages.success(request, 'Device registered successfully.')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')

        return redirect('add_devices')

    devices = DeviceRegistered.objects.filter(user_id=request.user.id)
    return render(request, 'startbootstrap/tables.html', {'devices': devices})

'''





"""

correctly working 





@login_required  # Ensure that the user is logged in
def add_devices(request):
    if request.method == "POST":
        serial_number = request.POST.get('serial_number')
        device_name = request.POST.get('device_name')
        
        # Debugging: Print values to ensure they're correct
        print("Serial Number:", serial_number)
        print("Device Name:", device_name)
        print("Username:", request.user.username)
        device_serv = serial_number.split('_')
        # Check if the device is already registered by the user
        if DeviceRegistered.objects.filter(user_id=request.user.id, device_id=serial_number).exists():
            messages.error(request, 'This device is already registered for your account.')
        else:
            # Attempt to register the device for the user
            try:
                DeviceRegistered.objects.create(
                    user_id=request.user.id,
                    username=request.user.username,  # Ensure it's a string, not a list
                    device_id='_'.join(serial_number.split('_')),  # Convert the serial number list into a string
                    device_name=device_name,
                    device_type=serial_number.split('_')[1] if '_' in serial_number else 'Unknown'
                )


                messages.success(request, 'Device registered successfully.')
            except Exception as e:
                messages.error(request, f'Error registering device: {e}')

        # Redirect to the same page to avoid resubmission
        return redirect('add_devices')  # Use the actual URL name defined in urls.py

    # Retrieve all registered devices for the logged-in user
    devices = DeviceRegistered.objects.filter(user_id=request.user.id)  # Fetch devices for the logged-in user
    return render(request, 'users/addDevices.html', {'devices': devices})

    


"""

"""



def add_devices(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        device_name = request.POST.get('device_name')
        device_type = DEVICE_TYPE  # Set your static device type here

        if serial_number and device_name:
            # Create a new DeviceRegistered instance
            new_device = DeviceRegistered(
                device_id=serial_number,
                device_name=device_name,
                device_type=device_type
            )
            try:
                new_device.save()  # Save the instance to the database
                messages.success(request, f"Device '{device_name}' with Serial Number '{serial_number}' registered successfully.")
            except IntegrityError as e:
                messages.error(request, "An error occurred while registering the device.")
                print(f"Error: {e}")
        else:
            messages.error(request, "Please enter valid serial number and device name.")

    devices = DeviceRegistered.objects.all()  # Retrieve all registered devices
    return render(request, 'users/addDevices.html', {'devices': devices})



"""




"""


def add_devices(request):
    serial_number = None  # Initialize a variable to store the serial number
    if request.method == 'POST':
        # Get the serial number from the POST data
        serial_number = request.POST.get('serial_number')
        if serial_number:
            # You can add more logic here (e.g., save the serial number or validate it)
            messages.success(request, f"Serial number {serial_number} entered successfully.")
        else:
            messages.error(request, "Please enter a valid serial number.")
    
    # Pass the serial number to the template
    return render(request, 'users/addDevices.html', {'serial_number': serial_number})


"""


@login_required

def remove_devices(request):
    context = {
        'header':'Remove Devices',
        'id':'Id',
        'Device_id':'Device ID',
        'Device_name':'Device Name',
        'Device_type':'Device Type',

    }
    return render(request, 'startbootstrap/tables.html', context)

