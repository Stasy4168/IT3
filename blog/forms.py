from django import forms
from .models import Post
from django.shortcuts import redirect

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)