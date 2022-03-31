from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# def index(request):
#     return JsonResponse({"hello": "world"})

def index(request):
    return render(request, 'index.html', context={'text': "Hello World"})

def example(request):
    return render(request, 'example.html', context={'text': "Hello World"})    