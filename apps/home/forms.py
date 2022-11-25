from django.contrib.admin import widgets
from django.forms import ModelForm, DateTimeInput
from django import forms
from apps.home.models import *

class DeporteForm(ModelForm):
    class Meta:
        model = Deporte
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_inicio'].widget.attrs['readonly'] = True