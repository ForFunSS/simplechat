from django import forms

class TextesForm(forms.Form):
    user = forms.CharField(max_length=30)
    text = forms.CharField(max_length=1000)
