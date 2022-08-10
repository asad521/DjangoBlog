from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SingupForm, LoginForm ,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth import logout as user_logout
from django.contrib.auth import login as user_login
from .models import Blogpost
# Create your views here.


def home(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


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
            user =form.save()
            group = Group.objects.get(name="Author")
            print(group)
            user.groups.add(group)
    else:
        form = SingupForm()
    return render(request, 'blog/signup.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        posts = Blogpost.objects.all()
        user = request.user
        fullname = user.get_full_name()
        groups = user.groups.all()
        print(groups)
        return render(request, 'blog/dashboard.html', {'posts': posts ,"groups":groups,
        "fullname":fullname})
    else:
        return HttpResponseRedirect('/login/')


def logout(request):
    print(request)
    user_logout(request)
    return HttpResponseRedirect('/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title =  form.cleaned_data['title']
                desc =  form.cleaned_data['desc']
                pst = Blogpost(title=title, desc=desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html' ,{'form':form})

    else:
        return HttpResponseRedirect('/login/')
    
    
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blogpost.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Blogpost.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
    
        
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blogpost.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    
    