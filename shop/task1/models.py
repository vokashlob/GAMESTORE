from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=9, decimal_places=3)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title