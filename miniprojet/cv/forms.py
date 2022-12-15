from django import forms


class FormConnexion(forms.Form):
    login = forms.CharField(max_length=10)
    mot2pass = forms.CharField (widget=forms.PasswordInput)