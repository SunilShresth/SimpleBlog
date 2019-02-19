from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})