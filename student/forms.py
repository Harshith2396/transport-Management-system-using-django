from django import forms
from .models import studs
opt=[
    ('male','Male'),
    ('female','Feamle'),
]

class stud_form(forms.ModelForm):
    usn=forms.CharField(label='University serial number',max_length=10)
    name=forms.CharField(max_length=50)
    father=forms.CharField(max_length=50)
    mother=forms.CharField(max_length=50)
    gender=forms.CharField(max_length=6,widget=forms.RadioSelect(choices=opt))
    college=forms.CharField(max_length=50)

    start=forms.CharField(max_length=50)
    destiantion=forms.CharField(max_length=50)
    changeover=forms.CharField(max_length=50)
    class Meta:
        model=studs
        fields=('usn','name','father','mother','gender','college','start','destiantion','changeover')

    