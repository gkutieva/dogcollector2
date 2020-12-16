from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Molly', 'husky', 'can speak small words', 5),
    Dog('Coco', 'maltese', 'fearless in a charming toy-dog way', 3),
    Dog('Axel', 'pug', 'stable temperament and great charm', 7),
    Dog('Cesar', 'long-hair chihuahua', 'hunt rats and other small animals', 10)
]

# Define our home view
def home(request):
    return HttpResponse('<h1>Hello Dog Lovers ໒(＾ᴥ＾)७</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})