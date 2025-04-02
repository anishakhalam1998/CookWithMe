"""form.py"""
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    """Reciepe form is created"""
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']
