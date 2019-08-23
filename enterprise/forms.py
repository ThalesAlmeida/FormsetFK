from django import forms
from django.forms import ModelForm
from .models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'linked_companies' : forms.CheckboxSelectMultiple()
        }