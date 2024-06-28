from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm , RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")

 
def login_view (request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_name= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user = authenticate(request , username=user_name , password=password)
        if user:
            login(request, user)
            return redirect("/")
        
    return render(request, 'profiels/form.html' , {'form':form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name= form.cleaned_data.get('username')
        email = form.cleaned_data.get('email ')
        password= form.cleaned_data.get('password')
        user = User.objects.create_user(user_name, email , password)
        user.save()
        login(request, user)
        return redirect("/")
    return render(request, 'profiels/form.html' , {'form':form})
        