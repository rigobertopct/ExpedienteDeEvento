# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class ModeloPrueba(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    class Meta:
        verbose_name="Prueba"
        verbose_name_plural="Pruebas"
# Create your models here.

