from django.shortcuts import render, HttpResponse
from . import models
from Course import models as hustle
from Book.models import Book
from Accounts.models import UserInfo


# Create your views here.
def auth_pages(request, str):
    if str == "register":
        return render(request, 'register.html')
    elif str == "login":
        return render(request, 'login.html')
    elif str == "edit-profile":
        if UserInfo.objects.filter(related_user=request.user).exists():
            info = UserInfo.objects.get(related_user=request.user)
            return render(request, 'edit-profile.html', {'info': info})
        else:
            return render(request, 'edit-profile.html', )

    elif str == "my-profile":
        if UserInfo.objects.filter(related_user=request.user).exists():

            info = UserInfo.objects.get(related_user=request.user)

            return render(request, 'my-profile.html', {'info': info})
        else:
            return render(request, 'edit-profile.html', )

def main_page(request):
    banner_image = models.home_page_banner.objects.all()
    main_header = models.header_title_main.objects.all()
    secondary_header = models.header_secondary_title.objects.all()
    sub_header = models.sub_header.objects.all()
    course_categories = hustle.Courses_categorie.objects.all()
    course = hustle.Course.objects.order_by('-created_at')
    books = Book.objects.order_by("-created_at")
    instructors = hustle.Our_Instructor.objects.all()
    offers = hustle.Course_Offers.objects.all()
    if request.user.is_authenticated:

            return render(request, 'main_page.html',
                          {'banner_image': banner_image, 'main_header': main_header,
                           'secondary_header': secondary_header, 'sub_header': sub_header,
                           'categories': course_categories, 'courses': course, 'books': books,
                           'instructors': instructors, 'offers':offers})

    else:
        return render(request, 'main_page.html',
                      {'banner_image': banner_image, 'main_header': main_header, 'secondary_header': secondary_header,
                       'sub_header': sub_header,
                       'categories': course_categories, 'courses': course, 'books': books, 'instructors': instructors})
