from django.db import models

# Create your models here.
class home_page_banner(models.Model):
    img = models.FileField(verbose_name="Home Banner Image")
    img_as_link = models.CharField(max_length=500, verbose_name="Image As link", null=True, blank=True)
    activate_shareble_link = models.BooleanField(default=False, verbose_name="Activate Shareable Link")
    def __str__(self):
        return self.img.name


class header_title_main(models.Model):
    main_header = models.CharField(max_length=350, verbose_name="Main headline")

    def __str__(self):
        return self.main_header


class header_secondary_title(models.Model):
    secondary_main_header = models.CharField(max_length=350, verbose_name="Secondary Main headline")

    def __str__(self):
        return self.secondary_main_header


class sub_header(models.Model):
    sub_header = models.CharField(max_length=350, verbose_name="Sub Title")

    def __str__(self):
        return self.sub_header