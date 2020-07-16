from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','pdf','cover_image']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        exclude=['']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
