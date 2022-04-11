from django.core import validators
from django import forms
from django.forms import widgets
from .models import User

class PersonnelForm(forms.ModelForm):
    class Meta:
        model =User
        fields = '__all__'
        widgets= {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }

