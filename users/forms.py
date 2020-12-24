from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.conf import settings


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=settings.GENDER_CHOICES,
                               widget=forms.Select(),
                               required=True)
    into = forms.ChoiceField(choices=settings.GENDER_CHOICES,
                                 widget=forms.Select(),
                                 required=True)
    status = forms.ChoiceField(choices=settings.STATUS_CHOICES,
                               widget=forms.Select(),
                               required=True)

    class Meta:
        model = Profile
        fields = ['age', 'gender', 'into', 'birth', 'region', 'school', 'major', 'status', 'tags', 'image']

