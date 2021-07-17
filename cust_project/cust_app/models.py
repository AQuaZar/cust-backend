from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ("A", "Одяг"),
    ("B", "Не Одяг"),
    ("C", "Шмодяг"),
)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField()
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name