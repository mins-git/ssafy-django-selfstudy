from django import forms
from .models import Diaries


class DiariesForm(forms.ModelForm):
    class Meta:
        model = Diaries
        fields = '__all__'