from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from pyuploadcare.dj.models import ImageField
import random
import string

CATEGORY_CHOICES = (
    ("A", "Одяг"),
    ("B", "Не Одяг"),
    ("C", "Шмодяг"),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ImageField(blank=True, default=None)
    slug = models.SlugField(blank=True, unique=True)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(self.image)
        if not self.slug:
            self.slug = slugify(self.name + "-" + rand_slug())
        super(Product, self).save(*args, **kwargs)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = ImageField(blank=True, default=None)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
