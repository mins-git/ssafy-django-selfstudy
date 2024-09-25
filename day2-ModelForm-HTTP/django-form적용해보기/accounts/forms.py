from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'maxlength': 12,
            }
        )
    )
    
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
    
    # class Meta:
    #     model = Todo
    #     fields = '__all__'