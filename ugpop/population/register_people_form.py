from django import forms 
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import Register_VHT,Register_People,Register_Birth,Report_Death

class PeopleForm(forms.ModelForm):
    class Meta:
        model=Register_People
        fields='__all__'
        # widgets = {
        #     'date': DateInput(attrs={'type': 'date'})
            
        # }

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        #self.helper = FormHelper()
        self.fields['UPIDN'].widget.attrs['readonly'] = True
        # self.fields["serial_number"].widget = HiddenInput()

