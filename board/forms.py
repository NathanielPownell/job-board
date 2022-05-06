from django import forms

from django.contrib.auth.models import User
from .models import Posting, Profile
from ckeditor.fields import RichTextField

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'rows': 5}))
    resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    skills = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'avatar', 'bio', 'resume', 'skills']


class CreatePostingForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-solid border-slate-400 border'}))
    desc = RichTextField()
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full border-solid border-slate-400 border', 'id': 'tags', 'placeholder': 'python,django,html,css,javascript'}))

    class Meta:
        model = Posting
        fields = ['title', 'desc', 'tags']


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': ' md:w-60 lg:w-96 md:text-xl lg:text-2xl w-60 text-xl border-2 border-slate-300', 'placeholder': '🔎 Search Job Titles...'}), label="")