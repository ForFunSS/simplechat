from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def message(request):
    messages = Textes.objects.all()
    index(request)
    return render(request, 'chat/messages.html', context={'messages': messages})

def index(request):
    userform = TextesForm()
    mess = Textes()
    messages = Textes.objects.all()
    if request.method == "POST":
        name = request.POST.get("user")
        textes = request.POST.get("text")

        mess.chat_user = name
        mess.chat_text = textes
        mess.save()

        return render(request, 'chat/messages.html', context={'messages': messages, "form": userform})


# Тут все просто, делаем mess моделью, и потом с помощью метода get берем значение из формы, и записывает в mess
# Значения chat_user и chat_text и сохраняем и под конец рендерим страницу.


# class PostPost():
#     def mess(self, request, username):
#         form = TextesForm(self.request.POST)
#         if form.is_valid():
#             Text = (text = form.cleanned_data['text'], user = form.cleanned_data['user'])
#             Text.save()
