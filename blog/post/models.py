from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(null=True) 

class Post(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title
# Create your models here.
