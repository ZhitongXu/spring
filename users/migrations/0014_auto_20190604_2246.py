# Generated by Django 2.2.1 on 2019-06-04 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190604_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2019, 6, 4, 22, 46, 54, 482050)),
        ),
    ]