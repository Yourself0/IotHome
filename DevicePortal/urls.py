from django.urls import path
from .views import DeviceSetting,add_devices, remove_devices

urlpatterns =[
    path('device_setting/', DeviceSetting.as_view(), name='device_setting'),
    path('add_devices/',  add_devices , name='add_devices'),  
    path('remove_devices/', remove_devices  , name='remove_devices'),
]