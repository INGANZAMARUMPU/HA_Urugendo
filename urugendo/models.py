from django.db import models
from django.contrib.auth.models import User

class Ingenzi(models.Model):
    id = models.BigAutoField(primary_key=True)
    izina = models.CharField(max_length=64)
    telephone = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "Ingenzi"

    def __str__(self) -> str:
        return f"{self.izina} {self.telephone}"

class Urugendo(models.Model):
    id = models.BigAutoField(primary_key=True)
    kuva = models.CharField(max_length=16)
    gushika = models.CharField(max_length=16)
    ibeyi = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.kuva} - {self.gushika} isaha {self.date}"

    class Meta:
        verbose_name_plural = "Ingendo"

class Itike(models.Model):
    id = models.BigAutoField(primary_key=True)
    ingenzi = models.ForeignKey(Ingenzi, on_delete=models.PROTECT)
    urugendo = models.ForeignKey(Urugendo, null=True, on_delete=models.SET_NULL)
    place = models.SmallIntegerField()
    date = models.DateTimeField()
    uwayimuhaye = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Amatike"
