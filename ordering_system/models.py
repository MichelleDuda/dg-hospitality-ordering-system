from django.db import models
from django.contrib.auth.models import AbstractUser

# Extension of User Model
class Student(AbstractUser):
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.SET_NULL, null=True, blank=True)
    
    #was receiving error after using AbstractUser class to add custom fields and found the following solution via chatgpt
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="student_set",  # Prevents clash with 'user_set'
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="student_permissions_set",  # Prevents clash with 'user_set'
        blank=True
    )

# Meal Plan Options
class MealPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
