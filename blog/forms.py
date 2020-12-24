from django import forms
from .models import Post, Comment
from django.conf import settings


class PostForm(forms.ModelForm):
    title = forms.ChoiceField(choices=settings.SOURCES_CHOICES,
                              widget=forms.Select(),
                              required=True)

    class Meta:
        model = Post
        fields = ['title', 'tags', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')