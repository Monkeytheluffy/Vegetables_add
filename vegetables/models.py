from django.db import models
from .mongodb import categories_collection, vegetables_collection  

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        category_data = {
            'name': self.name,
        }
        categories_collection.update_one({'name': self.name}, {'$set': category_data}, upsert=True)


class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='vegetables', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    offer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  

        vegetable_data = {
            'name': self.name,
            'category': self.category.name, 
            'description': self.description,
            'price': float(self.price),
            'weight': self.weight,
            'image': self.image.url if self.image else None, 
            'offer': self.offer,
        }

        vegetables_collection.update_one({'name': self.name}, {'$set': vegetable_data}, upsert=True)
