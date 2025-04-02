"""not used model.py"""
from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
    """not used"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
