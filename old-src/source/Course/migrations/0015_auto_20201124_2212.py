# Generated by Django 3.1.1 on 2020-11-24 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0014_auto_20201124_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 22, 12, 46, 929046, tzinfo=utc), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_linked',
            field=models.BooleanField(default=False, verbose_name='activate shareable link'),
        ),
    ]