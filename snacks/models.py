from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse 

# Create your models here.

class Snack(models.Model): 
    name = models.CharField(max_length=64) 
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default='') 

    def __str__(self): 
        """String for representing the MyModelName object (in Admin site effect.)."""
        return self.name 

    def get_absolute_url(self): 
        return reverse('snack_detail', args=[str(self.id)]) 