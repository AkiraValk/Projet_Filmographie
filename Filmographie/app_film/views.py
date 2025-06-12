from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import PersonnesForm
from . import models


def ajout_Personnes(request):
    form = PersonnesForm()
    return render(request, "app_film/ajout_Personnes.html", {"form":form})

def traitement_Personnes(request):
    pform = PersonnesForm(request.POST)
    if pform.is_valid():
        form = pform.save()
        return render(request,"app_film/affiche_Personnes.html",{"form" : form})
    else:
        return render(request,"app_film/ajout_Personnes.html",{"form": pform})


def affiche_Personnes(request):
    train = models.Personnes.objects.all()
    return render(request, "app_film/affiche_Personnes.html", {"train": train})

