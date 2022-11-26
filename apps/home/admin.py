# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from apps.home.models import *

admin.site.register(Deporte)
admin.site.register(Disciplina)
admin.site.register(Atleta)
admin.site.register(CodEvento)
admin.site.register(Partido)


