from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("please contact me")
def tracker(request):
    return HttpResponse("youre being tracked")
def search(request):
    return  HttpResponse("what you want to search ")

def productview(request):
    return HttpResponse("your product view")
def checkout(request):
    return HttpResponse("please checkout")
