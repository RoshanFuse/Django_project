from django import forms
from .models import Data

class ShowData(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','image']
        # labels = {'image':''}