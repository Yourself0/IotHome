from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from .models import DeviceState
from django.contrib.auth.decorators import login_required
from DevicePortal.models import DeviceRegistered
import logging


logger = logging.getLogger(__name__)








@login_required
def device_view(request):
    # Get the username of the logged-in user
    logged_in_username = request.user.username

    # Fetch devices registered by the logged-in user
    registered_devices = DeviceRegistered.objects.filter(username=logged_in_username)

    devices_with_buttons = []
    
    # Fetch all device states
  
    if not registered_devices.exists():
        print("No devices registered for this user.")

    # Construct the device data with button counts
    for device in registered_devices:
        try:
            button_count = int(device.device_type)  # Assuming device_type is convertible to int
        except (ValueError, TypeError):
            button_count = 0  # Default to 0 if conversion fails

        device_data = {
            'id': device.id,
            'device_id': device.device_id,
            'device_name': device.device_name,
            'device_type': device.device_type,
            'button_count': range(button_count)  # Generate range for button counts
        }
        devices_with_buttons.append(device_data)

    return render(request, 'users/deviceControl.html', {
        'devices': devices_with_buttons,
        'device_states': ""
    })





@login_required
def handle_device_click(request):
    if request.method == 'POST':
        # Retrieve the device name and button number
        device_name = request.POST.get('device')
        button_number = request.POST.get('button_number')

        # Ensure device name and button number are present
        if not device_name or button_number is None:
            logger.error('Device name or button number is missing.')
            return JsonResponse({'error': 'Device name or button number is missing'}, status=400)

        # Convert button_number to integer
        try:
            button_number = int(button_number)
        except ValueError:
            logger.error('Invalid button number: %s', button_number)
            return JsonResponse({'error': 'Invalid button number'}, status=400)

        # Create a dictionary to hold device_id mappings
        device_dict = {}
        
        # Retrieve all devices from DeviceRegistered
        device_states = DeviceRegistered.objects.all()
        for device in device_states:
            if device_name in device.device_name:
                device_dict[device.device_name] = device.id  # Map device_id to its corresponding id

        # Check if the device_id exists in the dictionary
        device_id = device_dict.get(device_name)
        if device_id is None:
            logger.error('Device not found: %s', device_name)
            return JsonResponse({'error': 'Device not found'}, status=404)

        # Retrieve or create the device state for the specific button using device_id
        device_state, created = DeviceState.objects.get_or_create(
            device_id=device_id,  # Use the device_id obtained from the dictionary
            button_number=button_number,
            user=request.user  # Set the current user as the owner
        )

        # Store the device name in the DeviceState object
        device_state.device_name = device_name  # Add this line to store the device name

        # Toggle the state based on the current state
        if device_state.state == "On":
            device_state.state = "Off"
        else:
            device_state.state = "On"

        # Save the updated state
        device_state.save()

        # Prepare the response
        response_data = {
            'message': f'Device {device_name} (ID: {device_id}) Button {button_number} is now {device_state.state}',
            'current_state': device_state.state,
            'logged_in_user_id': request.user.id
        }

        logger.info(f'Clicked {device_name} (ID: {device_id}) Button {button_number} with state {device_state.state}')
        return JsonResponse(response_data)

    logger.error('Invalid request method: %s', request.method)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
