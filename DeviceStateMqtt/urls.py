# urls.py
from django.urls import path
from .views import device_view, handle_device_click

urlpatterns = [
    path('devices/', device_view, name='device_view'),
    # path('get_initial_device_states/', get_initial_device_states, name='get_initial_device_states'),
    path('handle-device-click/', handle_device_click, name='handle_device_click'),


]
