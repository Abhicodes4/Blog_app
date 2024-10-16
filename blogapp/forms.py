from django import forms
from django.contrib.auth.models import User
from .models import BlogPost
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','tags']        

