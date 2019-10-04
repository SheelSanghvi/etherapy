from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, World. You're at polls index.")
def add(request,a,b):
	return HttpResponse("sum is {}".format(a+b))
def login(request,username):
	return HttpResponse("you have logged in successfully in account: {}".format(username))
	
# Create your views here.