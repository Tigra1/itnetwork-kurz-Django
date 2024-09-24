from django.shortcuts import render
from django.views import generic

from .models import Film

class FilmIndex(generic.ListView):

    template_name = "moviebook/film_index.html"  # cesta k šabloně ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "filmy"  # pod tímto jménem budeme volat seznam objektů v šabloně

# tato metoda nám získává seznam filmů seřazených od největšího id (9,8,7...)
    def get_queryset(self):
        return Film.objects.all().order_by("-id")