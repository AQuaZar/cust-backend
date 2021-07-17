from django.urls import path
from .views import ProductView


app_name = "cust_app"

urlpatterns = [
    path('test/', ProductView.as_view()),
]