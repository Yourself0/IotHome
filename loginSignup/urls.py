from django.urls import path

from DeviceStateMqtt import views as  DeviceStateMqttViews

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage, name= 'login'),
    path('logout/',views.logoutUser, name= 'logout'),
    path('register/', views.register, name='register'),
    path('devices/', DeviceStateMqttViews.device_view, name='Devices')
    
]