from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Poll
class UserRegisterForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','email','password1','password2']

class PollForm(forms.ModelForm):
    class Meta():
        model = Poll
        fields = ['questions', 'options_one', 'options_two', 'options_three', 'options_four']
        