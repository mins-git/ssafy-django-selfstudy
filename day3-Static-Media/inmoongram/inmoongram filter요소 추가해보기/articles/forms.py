from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '이미지 설명을 입력하세요'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }