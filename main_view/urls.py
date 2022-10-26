from django.urls import path
from . import views

urlpatterns = [
    path('View/<str:str>', views.auth_pages),
    path('', views.main_page),

]