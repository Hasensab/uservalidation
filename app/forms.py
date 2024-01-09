from django import forms
from app.models import *



def sname_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('it is started with a')

def sp_len(data):
    if len(data)<5:
        raise forms.ValidationError('length is lesser than 5 ')

class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[sname_a])
    sprinciple=forms.CharField(validators=[sname_a,sp_len])
    slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError('emails are not matched')
