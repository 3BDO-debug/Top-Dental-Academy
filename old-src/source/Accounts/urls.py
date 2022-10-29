from django.urls import path
from . import views
urlpatterns = [
    path('Run/<str:condition>', views.register_login_logout),
    path("Edit-Run/<str:condition>", views.edit_profile),
]