from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# do this later after creating models for home page ie models for training courses
#class IndexView(generic)

def index(request):
    return render(request, 'home/index.html')
    


def login_user(request):
    return render(request, 'authenticate/login.html', {})