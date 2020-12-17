from django.shortcuts import render
from .models import Dog

# Create your views here.
from django.http import HttpResponse

# Define our home view
def home(request):
    return HttpResponse('<h1>Hello Dog Lovers ໒(＾ᴥ＾)७</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})