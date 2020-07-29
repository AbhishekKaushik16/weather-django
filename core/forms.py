from django import forms

class Location(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your location'
    }))