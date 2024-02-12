from django.db import models



class Clients(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    discription = models.TextField()
    
    
    def __str__(self):
        return self.name

# Create your models here.
