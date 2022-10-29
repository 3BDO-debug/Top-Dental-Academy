# Generated by Django 3.1.1 on 2020-09-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_remove_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, default='First Name', max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, default='Last Name', max_length=30, null=True, verbose_name='Last name'),
        ),
    ]