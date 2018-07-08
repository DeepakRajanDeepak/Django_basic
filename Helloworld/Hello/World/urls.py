from django.urls import path
from World import views  
#import Worls view

urlpatterns = [
    path('', views.Home),
]
