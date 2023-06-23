from django import forms

class WhoisForm(forms.Form):
    domain = forms.CharField(label='', max_length=100)