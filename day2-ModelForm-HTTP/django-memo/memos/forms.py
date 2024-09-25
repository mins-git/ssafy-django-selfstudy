from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'summary',
            }
        )
    )
    memo = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder' : 'memo',
                'cols' : 50,
                'rows' : 5,
            }
            
        )
    )   
    
    
    class Meta:
        model = Memo
        fields = '__all__'