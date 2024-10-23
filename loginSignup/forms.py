from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from .models import Order

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'



class CreateUserForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Enter your first name.')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Enter your last name.')

    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']