# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Deporte(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre del deporte")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Deporte'
        verbose_name_plural = 'Deportes'
        db_table = 'deportes'


class Disciplina(models.Model):
    deporte = models.OneToOneField(
        Deporte,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre = models.CharField(max_length=250, verbose_name="Nombre de la disciplina")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'disciplina'
        db_table = 'disciplinas'