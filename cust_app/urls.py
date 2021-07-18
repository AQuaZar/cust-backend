from django.urls import path
from .views import ProductView, ProductDetail, AuthorView


app_name = "cust_app"

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('<slug:slug>/', ProductDetail.as_view())
]