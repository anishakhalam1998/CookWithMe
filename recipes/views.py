"""not used dfdf"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe  
from .forms import RecipeForm,CustomUserCreationForm
@login_required
def recipe_list(request):
    """not used"""
    recipes = Recipe.objects.all()  # Fetch all recipes
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    """not used"""
    recipe = get_object_or_404(Recipe, pk=pk)  # Fetch the recipe or raise 404
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_create(request):
    """not used"""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_update(request, pk):
    """not used"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.user != request.user:  # Check if the logged-in user owns the recipe
        return redirect('recipe_list')  # Redirect if not the owner
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    """not used"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.user != request.user:  # Check if the logged-in user owns the recipe
        return redirect('recipe_list')  # Redirect if not the owner
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

def home(request):
    """not used"""
    return render(request, 'home.html')

def signup(request):
    """Updated signup view with email and mobile"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set mobile in the profile
            user.userprofile.mobile = form.cleaned_data['mobile']
            user.userprofile.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})