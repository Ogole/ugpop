from django import forms 
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import Register_VHT,Register_People,Register_Birth,Report_Death

class BirthForm(forms.ModelForm):
    class Meta:
        model=Register_Birth
        fields='__all__'
