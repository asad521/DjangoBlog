from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SingupForm,LoginForm
# Create your views here.


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def login(request):
    form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})

def signup(request):
    form = SingupForm()
    return render(request, 'blog/signup.html', {'form':form})

def dashboard(request):
    return render(request, 'blog/dashboard.html')

def logout(request):
    return HttpResponseRedirect('/')