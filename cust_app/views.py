from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Author

# class CarSerializer(serializers.ModelSerializer):
#     photo_url = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Car
#         fields = ('id','name','price', 'photo_url')
#
#     def get_photo_url(self, car):
#         request = self.context.get('request')
#         photo_url = car.photo.url
#         return request.build_absolute_uri(photo_url)

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({"products": products})

