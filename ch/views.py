from django.shortcuts import render
from django.http import HttpResponse



def main_redirect(request):
    return HttpResponse('<h2> LOl </h2>')
