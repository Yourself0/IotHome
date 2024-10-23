from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"startbootstrap/index.html")



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or Password is Incorrect')
    context = {}
    return render(request,'startbootstrap/login.html',context )

def logoutUser(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('login')
            else:
                # Display the form errors for debugging
                messages.error(request, 'Please correct the errors below.')
        
    context = {'form': form}
    return render(request, 'startbootstrap/register.html', context)