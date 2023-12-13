from django import forms
from .models import CustomUser

class signupform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name','roles', 'email', 'number','password']

class loginform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email','password']