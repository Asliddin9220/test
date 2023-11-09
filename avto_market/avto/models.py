from django.db import models

# Create your models here.
class Avto(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    model = models.CharField(max_length=100)


    def __str__(self):
        return self.model
    

