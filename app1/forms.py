from cProfile import label
from tkinter import Widget
from xml.sax.xmlreader import AttributesImpl
from django import forms
from app1.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=(Student)
        fields="__all__"

GENDER=(
    ("1","male"),
    ("2","female"),
    ("3","others")
)

class UserInfo(forms.Form):
    name=forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email=forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    gender=forms.ChoiceField(choices=GENDER)
    contact=forms.IntegerField(label='mobile',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mobile'}))
