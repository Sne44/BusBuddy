# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Add an optional email field for better user contact management
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'})
    )

    class Meta:
        # Use the default User model
        model = User
        # The fields we want to show on the form
        fields = ('username', 'email', 'first_name', 'last_name')
        
    def save(self, commit=True):
        # Override save to ensure the email is saved
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user