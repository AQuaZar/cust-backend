from rest_framework import serializers
from .models import CATEGORY_CHOICES

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    image = serializers.ImageField()
    slug = serializers.SlugField()
    price = serializers.FloatField()
    category = serializers.CharField()