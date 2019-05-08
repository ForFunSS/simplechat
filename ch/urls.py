from django.urls import path, include
from .views import *

urlpattern = [
    path('lol/', index, name='index')
]
