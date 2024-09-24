from django.db import models

# Create your models here.
# pojistenci/models.py
from django.db import models

class Pojisteny(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    vek = models.IntegerField()
    telefon = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, Telefon: {self.telefon}"
