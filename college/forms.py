from django import forms
from .models import college
class formc(forms.ModelForm):
    name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=10)
    address=forms.Textarea()

    class Meta:
        model=college
        fields=('name','email','phone','address')
