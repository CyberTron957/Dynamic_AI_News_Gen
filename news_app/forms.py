from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pincode', 'image']  
        widgets = {
            'pincode': forms.TextInput(attrs={'required': 'required'}),
        }