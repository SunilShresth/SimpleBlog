from django.shortcuts import render

# do this later after creating models for home page ie models for training courses
#class IndexView(generic)

def index(request):
    return render(request, 'home/index.html')