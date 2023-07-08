from django.shortcuts import render,HttpResponse

# Create your views here.

def routes(request):
    return HttpResponse("Hi")