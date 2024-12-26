from django.shortcuts import render
from .models import Chaivariety
from django.shortcuts import get_object_or_404



# Create your views here.
def all_apps(request):
    chais = Chaivariety.objects.all()
    return render(request,'all/all_new_app.html',{'chais':chais})   
def all_detail(request,all_id):
    chai = get_object_or_404(Chaivariety,pk=all_id)
    return render(request,'all/all_detail.html',{'chai':chai}) 
 