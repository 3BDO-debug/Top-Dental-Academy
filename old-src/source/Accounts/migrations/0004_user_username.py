# Generated by Django 3.1.1 on 2020-09-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20200909_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=350, verbose_name='Username'),
            preserve_default=False,
        ),
    ]