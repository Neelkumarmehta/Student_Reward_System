from django import forms
from CRUDOperation.models import StuModel

class Stuforms(forms.ModelForm):
    class Meta:
     model=StuModel
     fields="__all__"