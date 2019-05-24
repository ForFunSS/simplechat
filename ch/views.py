from django.shortcuts import render
from .forms import *
from .models import Textes

def message(request):
    messages = Textes.objects.all()
    return render(request, 'chat/messages.html', context={'messages': messages})

class MessageCreate(View):
    def get(self, reqiest):
        form = MessageForm()
        return render(request, )
