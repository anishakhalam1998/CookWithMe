import pytest
from django.contrib.auth.models import User
from recipes.models import Recipe



@pytest.mark.django_db
def test_create_recipe():
    # Create a user
    user = User.objects.create_user(username="testuser", password="testpassword")
    
    # Create a recipe
    recipe = Recipe.objects.create(
        user=user,
        title="Test Recipe",
        description="A test recipe description.",
        ingredients="1 cup flour, 2 eggs",
        instructions="Mix and bake.",
    )
    
    # Check if the recipe is created correctly
    assert recipe.title == "Test Recipe"
    assert recipe.description == "A test recipe description."
    assert recipe.ingredients == "1 cup flour, 2 eggs"
    assert recipe.instructions == "Mix and bake."
    assert recipe.user == user


@pytest.mark.django_db
def test_recipe_string_representation():
    # Create a user
    user = User.objects.create_user(username="testuser", password="testpassword")
    
    # Create a recipe
    recipe = Recipe.objects.create(
        user=user,
        title="Test Recipe",
        description="A test recipe description.",
        ingredients="1 cup flour, 2 eggs",
        instructions="Mix and bake.",
    )
    
    # Check if string representation returns the title
    assert str(recipe) == "Test Recipe"


@pytest.mark.django_db
def test_recipe_user_relationship():
    # Create a user
    user = User.objects.create_user(username="testuser", password="testpassword")
    
    # Create a recipe
    recipe = Recipe.objects.create(
        user=user,
        title="Test Recipe",
        description="A test recipe description.",
        ingredients="1 cup flour, 2 eggs",
        instructions="Mix and bake.",
    )
    
    # Check the user relation
    assert recipe.user.username == "testuser"
    assert recipe.user.email == ""  # or the email of the user if set


@pytest.mark.django_db
def test_recipe_delete_user_cascade():
    # Create a user
    user = User.objects.create_user(username="testuser", password="testpassword")
    
    # Create a recipe
    recipe = Recipe.objects.create(
        user=user,
        title="Test Recipe",
        description="A test recipe description.",
        ingredients="1 cup flour, 2 eggs",
        instructions="Mix and bake.",
    )
    
    # Delete the user
    user.delete()
    
    # Check if the recipe is also deleted (due to the on_delete=models.CASCADE)
    assert not Recipe.objects.filter(id=recipe.id).exists()
