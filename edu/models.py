from django.db import models
from datetime import datetime

# Create your models here.
class Matricula(models.Model):
    matricula = models.IntegerField()
    nome_aluno = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    observacao = models.TextField()
    data_matricula = models.DateTimeField(verbose_name='Data de matrícula', blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Matrícula de Aluno'
        verbose_name_plural = 'Matrículas de Alunos'
        ordering = ['nome_aluno']
