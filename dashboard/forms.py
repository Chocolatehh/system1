from django import forms
from .models import WenWu, Category


class WenWuForm(forms.ModelForm):
    class Meta:
        model = WenWu
        fields = '__all__'
        exclude = ['created_at']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['created_at']
