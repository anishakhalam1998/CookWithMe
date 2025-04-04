from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Recipe

class CustomUserCreationForm(UserCreationForm):
    """Extends UserCreationForm with email and mobile"""
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    mobile = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Enter a valid mobile number.")],
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Mobile will be saved via the UserProfile signal
        return user

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