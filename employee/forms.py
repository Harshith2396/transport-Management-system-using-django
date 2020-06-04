from django import forms
from college.models import college
class formc(forms.ModelForm):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    class Meta:
        model=college
        fields=('username','password')
