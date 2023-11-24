from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Medico(AbstractUser):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=127, unique=True, error_messages={"unique": "Este campo deve ser único."})
    senha = models.CharField(max_length=127)
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=80)
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=60)

    
