# Generated by Django 3.1.1 on 2020-09-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_auto_20200914_1347'),
        ('Accounts', '0006_auto_20200914_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='purchased_courses',
            field=models.ManyToManyField(to='Course.Course', verbose_name='Purchased Courses'),
        ),
    ]