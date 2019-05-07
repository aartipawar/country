from .models import *
from django import forms
from django.forms import ModelForm

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city','state']
        labels = {
            'city':('City'),
            'state':('State')
        }  
        widgets = {
            
            'city': forms.Select(attrs={'class': 'form-control','required': True}),
            'state': forms.Select(attrs={'class': 'form-control','required': True}),    
        } 


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state','country']
        labels = {
            'state':('State'),
            'country':('Country')
        }  
        widgets = {
            
            'state': forms.Select(attrs={'class': 'form-control','required': True}),
            'country': forms.Select(attrs={'class': 'form-control','required': True}),    
        } 


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country']
        labels = {
            'country':('Country'),    
        }  
        widgets = {
            
            'country': forms.Select(attrs={'class': 'form-control','required': True}),    
        } 

