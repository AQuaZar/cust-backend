from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product, Author
import json

# class ProductSerializer(serializers.ModelSerializer):
#     photo_url = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Product
#         fields = ('id','name','description','price', 'photo_url','slug','category')
#
#     def get_photo_url(self, product):
#         request = self.context.get('request')
#         photo_url = product.image.url
#         return request.build_absolute_uri(photo_url)

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialized_array = []
        for product in products:
            print('In view',product.image)
            image = product.image
            serializer = ProductSerializer(product)
            serialized_data = dict()
            for k,v in serializer.data.items():
                serialized_data[k]=v
            serialized_data['image'] = str(image)
            print('After serializer ', serializer.data)
            serialized_array.append(serialized_data)
        return Response(json.dumps(serialized_array))

