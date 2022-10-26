from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from Course.models import Course


# Create your models here.
class Accounts_Manager(BaseUserManager):
    def create_user(self, email, full_name, key, is_active,
                    password):
        if not email:
            raise ValueError("user must have email address")

        if not password:
            raise ValueError("password cannot be Null")

        user = self.model(email=self.normalize_email(email), full_name=full_name, key=key,
                          is_active=True, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user_super(self, email, full_name, password):
        if not email:
            raise ValueError("user must have email address")

        user = self.model(email=self.normalize_email(email), full_name=full_name, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user_super(full_name=full_name, email=email, password=password, )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=500, verbose_name="Full Name")
    email = models.EmailField(max_length=60, default="email@example.com", unique=True)
    key = models.CharField(max_length=1500, verbose_name="User Secret Key", default="Secret Key")
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, )
    user_purchased_courses = models.ManyToManyField(Course)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True, )
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, verbose_name='Approve account')
    status = models.CharField(max_length=150, default="Online")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]
    objects = Accounts_Manager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserInfo(models.Model):
    related_user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name="First name", default="First Name", blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name="Last name", default="Last Name", blank=True, null=True)

    mobile = models.CharField(max_length=300, default="Phone Number", blank=True, null=True)
    number = models.CharField(max_length=350, blank=True, default="Address", null=True)
    street = models.CharField(max_length=350, blank=True, default="Address", null=True)
    city = models.CharField(max_length=350, blank=True, default="Address", null=True)
    country = models.CharField(max_length=350, blank=True, default="Address", null=True)

    def __str__(self):
        return self.related_user.full_name
