from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
            'password1': forms.PasswordInput(attrs={'placeholder': "Password"}),
            'password2': forms.PasswordInput(attrs={'placeholder': "Confirm Password"})

        }

        def save(self , commit=True):
            user = super(UserForm).save(commit=False)
            if commit:
                user.save()
                return user