from django.shortcuts import render
from .models import *

def main_page(request):
    return render(request,'chat/index.html')

def message_list(request):
    messages = Textes.objects.all()
    return render(request, 'chat/index.html', context={'messages': messages})
