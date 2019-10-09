from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=45, null=False, blank=False)
    genero = models.CharField(max_length=25, null=False, blank=False)
    autor = models.CharField(max_length=50, null=False, blank=False)
    
