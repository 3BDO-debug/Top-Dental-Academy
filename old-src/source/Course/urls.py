from django.urls import path
from . import views

urlpatterns = [
    path('View/Courses/Categories/<int:id>', views.courses_categories),
    path('View/Intro/<int:id>', views.course_intro_view),
    path('View/Course/Content/<int:id>', views.course_content)
]