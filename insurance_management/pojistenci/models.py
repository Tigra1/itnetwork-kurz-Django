

# Tvorba modelů.

from django.db import models

class Pojisteny(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    vek = models.IntegerField()
    telefon = models.CharField(max_length=13)

    def __str__(self):
        return f"Název: {self.jmeno}, Cena: {self.prijmeni} KČ, {self.vek} ks., EAN: {self.telefon}"
