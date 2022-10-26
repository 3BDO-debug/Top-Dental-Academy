from django.db import models
from Accounts.models import User
from Course.models import Course
# Create your models here.
class Order(models.Model):
    order_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order_relationship", verbose_name="Order Owner")
    ordered_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Order_Course_relationship", verbose_name="Ordered Course")
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")