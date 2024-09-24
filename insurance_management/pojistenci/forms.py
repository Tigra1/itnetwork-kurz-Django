# pojistenci/forms.py
from django import forms
from .models import Pojisteny

class PojistenyForm(forms.ModelForm):
    class Meta:
        model = Pojisteny
        fields = ['jmeno', 'prijmeni', 'vek', 'telefon']
