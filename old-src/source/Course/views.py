from django.shortcuts import render, redirect
from . import models
from Accounts.models import User 

# Create your views here.

def courses_categories(request, id):
    course_categories = models.Courses_categorie.objects.all()

    all_category_courses = models.Course.objects.filter(related_category=id)
    return render(request, 'courses-list.html', {'courses': all_category_courses, 'categories': course_categories})


def course_intro_view(request, id):
    course_categories = models.Courses_categorie.objects.all()
    offers = models.Course_Offers.objects.all()
    course_info = models.Course.objects.get(id=id)
    related_courses = models.Course.objects.filter(related_category=course_info.related_category)
    if request.user.is_authenticated:
        if request.user.user_purchased_courses.filter(id=id).exists():
            return render(request, 'course-resume.html',
                          {'course_info': course_info, 'related_courses': related_courses,
                           'categories': course_categories, 'offers': offers})
        else:
            return render(request, 'course-intro.html',
                          {'course_info': course_info, 'categories': course_categories, 'offers': offers})
    else:
        return render(request, 'course-intro.html',
                      {'course_info': course_info, 'categories': course_categories, 'offers': offers})


def course_content(request, id):
    if request.user.is_authenticated:
            for purchased_course in request.user.user_purchased_courses.all():
                if purchased_course.id == id:

                    content = models.Course.objects.get(id=id)
                    return render(request, 'course-lesson-1.html', { 'content': content})
            return redirect('/')
                    
        
    else:
        return redirect('/')


