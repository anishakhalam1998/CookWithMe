"""form.py"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from .models import Recipe

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Enter a valid mobile number.")],
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "mobile", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        username = self.cleaned_data.get('username')

        # Check if password is too similar to username
        if username and password1.lower() == username.lower():
            raise ValidationError("Password cannot be too similar to your username.")

        # Minimum length check
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        # Check for at least one number
        if not re.search(r'\d', password1):
            raise ValidationError("Password must contain at least one number.")

        # Check for at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise ValidationError("Password must contain at least one special character.")

        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match.")

        return cleaned_data
class RecipeForm(forms.ModelForm):
    """Reciepe form is created"""
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        ingredients = cleaned_data.get('ingredients')
        instructions = cleaned_data.get('instructions')

        if not title:
            self.add_error('title', 'This field can\'t be empty')
        if not description:
            self.add_error('description', 'This field can\'t be empty')
        if not ingredients:
            self.add_error('ingredients', 'This field can\'t be empty')
        if not instructions:
            self.add_error('instructions', 'This field can\'t be empty')

        return cleaned_data