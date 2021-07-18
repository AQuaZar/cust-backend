from rest_framework import serializers
from pyuploadcare.dj.models import ImageField
from .models import CATEGORY_CHOICES
from django.contrib.auth.models import User


class CurrentUserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name')

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    user = CurrentUserSerializer()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    color = serializers.CharField()
    image = ImageField()
    slug = serializers.SlugField()
    price = serializers.FloatField()
    category = serializers.CharField()