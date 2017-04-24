from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def detail_category(request, category_id):
    return HttpResponse("You're looking at category %s." % category_id)


def home(request):
    return render(request, 'mainapp/home.html')