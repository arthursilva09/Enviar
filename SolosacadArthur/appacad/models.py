from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=150)

class Sala(models.Model):
    nome = models.CharField(max_length=150)
    professor = models.ForeignKey('Professor',on_delete="PROTECT")
