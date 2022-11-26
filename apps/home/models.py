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
    nombre = models.CharField(max_length=250, verbose_name="Nombre de la disciplina")
    deporte_id = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'
        db_table = 'disciplinas'


class CodEvento(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre de la disciplina")
    descripcion = models.CharField(max_length=1000, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'codEvento'
        verbose_name_plural = 'codEventos'
        db_table = 'codEventos'


class Pais(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre de la disciplina")
    sigla = models.CharField(max_length=250, verbose_name="Siglas")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'paises'


class Atleta(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre")
    apel = models.CharField(max_length=250, verbose_name="Apellido")
    apel = models.CharField(max_length=250, verbose_name="Apellido")
    fecha = models.DateField(verbose_name="Fecha de Nacimiento")
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'atletas'
        verbose_name_plural = 'atletas'
        db_table = 'atletas'


class Participacion(models.Model):
    evento_id = models.ForeignKey(CodEvento, on_delete=models.SET_NULL, null=True, blank=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True)
    atleta_id = models.ForeignKey(Atleta, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = 'participacion'
        verbose_name_plural = 'participacions'
        db_table = 'participacions'

class Partido(models.Model):
    atleta_id = models.ForeignKey(Atleta, on_delete=models.SET_NULL, null=True, blank=True)
    result = models.CharField(max_length=250, verbose_name="Resultado")
    observaciones = models.CharField(max_length=10000, verbose_name="Observaciones")
    class Meta:
        verbose_name = 'partido'
        verbose_name_plural = 'partidos'
        db_table = 'partidos'