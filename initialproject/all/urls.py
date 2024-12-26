

from django.urls import path
from  all import views  

urlpatterns = [
    path('', views.all_apps,name='all_app'),
    path('<int:all_id>', views.all_detail,name='all_detail'),
    
]
  