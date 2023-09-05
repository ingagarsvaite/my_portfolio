from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def home(response):
    return render(response, "ingosapp/home.html", {})

def author(response):
    return render(response, "ingosapp/author.html", {})

def foodscience(response):
    return render(response, "ingosapp/foodscience.html", {})

def foodapp(response):
    return render(response, "ingosapp/foodapp.html", {})

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=id)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.pavadinimas, str(item.tekstas)))


# Create your views here.
