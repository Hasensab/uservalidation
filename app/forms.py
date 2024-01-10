from django import forms
from app.models import *

from django.core import validators#performing built-in validators

def sname_a(data):#performing validation using normal functions
    if data.lower().startswith('a'):
        raise forms.ValidationError('it is started with a')

def sp_len(data):#performing validation using normal functions
    if len(data)<5:
        raise forms.ValidationError('length is lesser than 5 ')

class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[sname_a,validators.MinLengthValidator(4)])
    sprinciple=forms.CharField(validators=[sname_a,sp_len])
    slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    repass=forms.CharField(widget=forms.PasswordInput)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)
    def clean(self):#performing validation using form object method 'clean'
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        p=self.cleaned_data['password']
        rp=self.cleaned_data['repass']
        if e!=re or p!=rp:
            raise forms.ValidationError('emails are not matched')
    def clean_botcatcher(self):#performing validation using form object method 'clean_element'
        a=self.cleaned_data['botcatcher']
        if len(a)>0:
            raise forms.ValidationError('bot is catched')
