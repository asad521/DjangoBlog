from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SingupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                print(user)
                if user is not None:
                    user_login(request, user)
                    print('success')
                    messages.success(request, "You are successfully logged-in")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    return HttpResponseRedirect('/dashboard/')




def signup(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation! You have become author")
            form.save()
    else:
        form = SingupForm()
    return render(request, 'blog/signup.html', {'form': form})


def dashboard(request):
    return render(request, 'blog/dashboard.html')


def logout(request):
    return HttpResponseRedirect('/')
