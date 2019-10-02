from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, World. You're at polls index.")
def add(request,a,b):
	return HttpResponse("sum is {}".format(a+b))
	
# Create your views here.