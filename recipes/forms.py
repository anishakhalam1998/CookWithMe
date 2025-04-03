"""form.py"""
from django import forms
from .models import Recipe

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