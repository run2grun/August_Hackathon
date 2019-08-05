from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request,'location.html')

def parse(requset):
    return render(request, 'parsing.html'