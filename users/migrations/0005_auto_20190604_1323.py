# Generated by Django 2.2.1 on 2019-06-04 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190604_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2019, 6, 4, 13, 23, 22, 543766)),
        ),
    ]