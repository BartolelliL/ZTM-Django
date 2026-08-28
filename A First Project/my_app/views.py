from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World...")

def about(request):
    return HttpResponse("<h1>My name is Bartox<h1>")

def hello(request, first_name: str):
    return HttpResponse(f"Hello {first_name}")

def addition(request, num_1: int, num_2: int):
    if num_1 + num_2 == 1:
        return HttpResponse(f"I have {num_1 + num_2} pizza in the kitchen.")
    else:
        return HttpResponse(f"I have {num_1 + num_2} pizzas in the kitchen.")