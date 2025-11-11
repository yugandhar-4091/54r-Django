from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleinfo(request):
    data={"name":'yugandhar','age':24,'city':"vizag"}
    return JsonResponse(data)

def dynamicresponce(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city",'')
    return HttpResponse(f"hello {name} from {city}")