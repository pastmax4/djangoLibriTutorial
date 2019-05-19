from django.db import models

# Create your models here.

class libro(models.Model):
    titolo = models.TextField(blank=True,null=True)
    autore = models.TextField(blank=True,null=True)
    prezzo = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True, null=True)

