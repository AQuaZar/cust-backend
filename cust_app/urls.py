from django.urls import path
from .views import ProductView, ProductDetail


app_name = "cust_app"

urlpatterns = [
    path('test/', ProductView.as_view()),
    path('<slug:slug>/', ProductDetail.as_view())
]