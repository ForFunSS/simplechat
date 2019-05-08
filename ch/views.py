from django.shortcuts import render
from .models import *

def index(request):
    ch_text = Text.object(chat_text).all()
    ch_name = Text.chat_name.all()

    return render(request, 'index.html', context={'ch_text':ch_text, 'ch_name':ch_name})
