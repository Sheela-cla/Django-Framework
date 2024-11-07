from django.forms import ModelForm
from django import forms
from basicapp.models import UserInfo

class FormName(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = UserInfo
        fields = ['name','email','text']
