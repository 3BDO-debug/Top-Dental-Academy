from django.db import models
from django.utils import timezone


class Courses_categorie(models.Model):
    category = models.CharField(max_length=250, verbose_name="Course Category")

    def __str__(self):
        return self.category


class Courses_Video(models.Model):
    topic_name = models.CharField(
        max_length=350, verbose_name="Topic Name", default="Course Topic Name"
    )
    video = models.CharField(
        max_length=3500, verbose_name="Video Name", default="Lecture.mp4"
    )
    # video = ModelAdminResumableFileField()

    def __str__(self):
        return self.video


class Course_Offers(models.Model):
    offer_title = models.CharField(
        max_length=350,
        verbose_name="Offer Title",
        default="Title",
    )
    offer_body = models.TextField(
        verbose_name="Offer Body", default="Offer Body goes here"
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.offer_title


class Courses_video_link(models.Model):
    topic_name = models.CharField(
        max_length=350, verbose_name="Topic Name", default="Course Topic Name"
    )
    video_youtube_link = models.CharField(
        max_length=500, verbose_name="Video Youtube Link"
    )

    def __str__(self):
        return self.video_youtube_link


class Course_promo(models.Model):
    video = models.FileField(verbose_name="Course Promo Video")
    video_youtube_link = models.CharField(
        max_length=700,
        verbose_name="Youtube Optional Promo Link",
        null=True,
        blank=True,
    )
    activate_shareable_link = models.BooleanField(default=False, verbose_name="Activate Shareable Link")
    def __str__(self):
        return self.video.name


class Course_objective(models.Model):
    course_objectives = models.CharField(
        max_length=350, verbose_name="Course Objectives"
    )

    def __str__(self):
        return self.course_objectives


class Course(models.Model):
    related_category = models.ForeignKey(
        Courses_categorie, on_delete=models.CASCADE, related_name="Categoryrelationship"
    )
    course_name = models.CharField(max_length=350, verbose_name="Course Name")
    short_desc = models.CharField(
        max_length=400,
        verbose_name="Course Short Description (will be displayed in the main page)",
    )
    course_promo = models.ForeignKey(
        Course_promo,
        on_delete=models.CASCADE,
        verbose_name="Course Promo Video",
        null=True,
    )
    course_objectives = models.ManyToManyField(
        Course_objective, verbose_name="Course Objectives", related_name="first"
    )
    course_objectives2 = models.ManyToManyField(
        Course_objective, verbose_name="Course Objectives", related_name="second"
    )

    desc = models.TextField(verbose_name="Course Full Description")
    course_instructor = models.CharField(
        max_length=350, verbose_name="Course Instructor Name"
    )
    num_of_lectures = models.IntegerField(verbose_name="Number of Course Lecture")
    course_thumbnail = models.ImageField(verbose_name="Course Thumbnail.")
    course_thumbnail_as_link = models.CharField(max_length=500, verbose_name="Course's thumbnail as link", blank=True, null=True)
    course_price = models.CharField(
        max_length=350, verbose_name="Course Price", default="EGP 0.00"
    )
    sale_price = models.CharField(
        max_length=350,
        verbose_name="Sale Price",
        blank=True,
        null=True,
        default="EGP 0.00",
    )
    content = models.ManyToManyField(Courses_Video, verbose_name="Course Content", null=True, blank=True)
    youtube_content = models.ManyToManyField(
        Courses_video_link,
        verbose_name="Youtube Optional Content Upload",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(verbose_name="Created At", default=timezone.now())
    is_free = models.BooleanField(default=False, verbose_name="Free Course")
    sale = models.BooleanField(default=False, verbose_name="Activate Sale")
    is_linked = models.BooleanField(default=False, verbose_name="activate shareable link")
    
    def __str__(self):
        return self.course_name


class Our_Instructor(models.Model):
    name = models.CharField(max_length=350, verbose_name="Instructor Name")
    img = models.ImageField(verbose_name="Instructor Image")

    def __str__(self):
        return self.name
