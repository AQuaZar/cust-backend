from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Author

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({"products": products})

