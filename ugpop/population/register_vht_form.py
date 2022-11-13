from django import forms 
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput
from .models import Register_VHT,Register_People,Register_Birth,Report_Death

class VHTForm(forms.ModelForm):
    class Meta:
        model=Register_VHT
        fields='__all__'
        # widgets = {
        #     'date': DateInput(attrs={'type': 'date'})
            
        # }

    def __init__(self, *args, **kwargs):
        super(VHTForm, self).__init__(*args, **kwargs)
        #self.helper = FormHelper()
        self.fields['VHTIDN'].widget.attrs['readonly'] = True
        # self.fields["serial_number"].widget = HiddenInput()


