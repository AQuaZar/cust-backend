from rest_framework import serializers
from pyuploadcare.dj.models import ImageField
from .models import CATEGORY_CHOICES

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    color = serializers.CharField()
    image = ImageField()
    slug = serializers.SlugField()
    price = serializers.FloatField()
    category = serializers.CharField()