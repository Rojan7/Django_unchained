from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    # return HttpResponse('Start of the django sries. this is home page')
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def contact(request):
    return render(request,'website/contact.html')

