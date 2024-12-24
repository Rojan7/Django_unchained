from django.shortcuts import render
from .models import Chaivariety



# Create your views here.
def all_apps(request):
    chais = Chaivariety.objects.all()
    return render(request,'all/all_new_app.html',{'chais':chais})    
