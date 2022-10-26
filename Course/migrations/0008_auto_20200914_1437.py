# Generated by Django 3.1.1 on 2020-09-14 14:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0007_auto_20200914_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_title', models.CharField(default='Title', max_length=350, verbose_name='Offer Title')),
                ('offer_body', models.TextField(default='Offer Body goes here', verbose_name='Offer Body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 14, 37, 27, 545125, tzinfo=utc), verbose_name='Created At'),
        ),
    ]