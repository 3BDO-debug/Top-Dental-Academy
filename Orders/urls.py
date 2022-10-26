from django.urls import path
from . import views

urlpatterns = [
    path('Place/order/<int:id>', views.create_order)
]