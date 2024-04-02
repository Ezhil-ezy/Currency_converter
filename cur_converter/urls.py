from django.urls import path
from . import views 


urlpatterns = [
    path('', views.chrome, name = 'chrome') ,
    path('add', views.add, name = 'add'),
    path('addition', views.addition, name = 'addition')
    
] 