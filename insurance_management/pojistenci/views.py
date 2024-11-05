from django.shortcuts import render

# Create your views here.
# pojistenci/views.py
from django.shortcuts import render, redirect
from .models import Pojisteny
from .forms import PojistenyForm

def home(request):
    query = request.GET.get('q')  # Získání vyhledávacího řetězce
    if query:
        # Pokud existuje požadavek na vyhledávání, filtruje seznam podle jména nebo příjmení
        pojistencis = Pojisteny.objects.filter(jmeno__icontains=query) | Pojisteny.objects.filter(prijmeni__icontains=query)
    else:
        # Pokud nedojde k vyhledání, zobrazíme všechny pojištěnce
        pojistencis = Pojisteny.objects.all()

    return render(request, 'pojistenci/home.html', {'pojistencis': pojistencis})
def add_pojisteny(request):
    if request.method == "POST":
        form = PojistenyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pojistencu')
    else:
        form = PojistenyForm()
    return render(request, 'pojistenci/add_pojisteny.html', {'form': form})

def list_pojistencu(request):
    pojistenci = Pojisteny.objects.all()
    return render(request, 'pojistenci/list_pojistencu.html', {'pojistenci': pojistenci})
