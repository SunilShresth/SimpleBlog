from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm

# do this later after creating models for home page ie models for training courses
#class IndexView(generic)

def index(request):
    return render(request, 'home/index.html', {})
    


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, ('Error in logging in.. please try again!'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been successfully logged out!'))
    return redirect('login')

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password = password)
            # login(request, user)
            messages.success(request, ('You have successfully Signed up!!'))
            return redirect('login')
        else:
            messages.error(request, ('Your form is not validated! Try again!!'))
            return redirect('signup')

    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authenticate/signup.html', context)