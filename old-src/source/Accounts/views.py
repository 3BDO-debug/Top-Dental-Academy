from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, UserInfo
from django.contrib import messages


# Create your views here.
def register_login_logout(request, condition):
    if condition == "register":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        key = request.POST.get("key")

        if password != confirm_password:
            messages.error(request, "Password Doesn't Match")
            return redirect("/View/register")
        elif password == confirm_password:
            if User.objects.filter(email=email).exists():
                body = "Hey" + " " + full_name + "Account with this email already exists, you may want to login instead? "
                messages.error(request, body)
                return redirect('/View/register')
            elif User.objects.filter(full_name=full_name).exists():
                body1 = "Hey" + " " + full_name + " " + "Account with your name Already Exists. Login now"
                messages.error(request, body1)
                return redirect("/View/register")
            elif not User.objects.filter(email=email).exists() and not User.objects.filter(
                    full_name=full_name).exists():
                User.objects.create_user(full_name=full_name, email=email, key=key.split("/")[1], password=password,
                                         is_active=True).save()
                UserInfo.objects.create(related_user=User.objects.get(email=email)).save()
                body2 = "Nice" + " " + full_name + " " + "Your Account had been created successfully login now"
                return redirect('/View/login')
    elif condition == "login":
        email = request.POST.get("email")
        password = request.POST.get("password")
        key = request.POST.get("key")

        check = authenticate(request, email=email, password=password)
        if check:
            get_user = User.objects.get(email=email)
            if get_user.key > key.split("/")[1]:
                if get_user.key.split("/")[1] == key.split("/")[1]:
                    login(request, check)
                    return redirect("/")
            elif get_user.key == key.split("/")[1]:
                login(request, check)
                return redirect("/")

            else:
                messages.error(request,
                               "We Are Sorry, you cant access your account from another device than the one you registered from")
                return redirect('/View/login')
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect('/View/login')
    elif condition == "logout":
        logout(request)
        return redirect('/')


def edit_profile(request, condition):
    get_user = UserInfo.objects.get(related_user=request.user)
    if condition == "edit-contact":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile = request.POST.get("mobile")
        get_user.first_name = first_name
        get_user.last_name = last_name
        get_user.save()

        get_user.mobile = mobile
        return redirect('/View/my-profile')

    elif condition == "edit-profile-photo":
        profile_pic = request.FILES.get("profile_pic")
        get_user.profile_pic = profile_pic
        get_user.save()
        return redirect('/View/my-profile')

    elif condition == "address-info":
        number = request.POST.get("number")
        street = request.POST.get("street")
        city = request.POST.get("city")
        country = request.POST.get("country")

        get_user.number = number
        get_user.street = street
        get_user.city = city
        get_user.country = country
        get_user.save()
        return redirect('/View/my-profile')
