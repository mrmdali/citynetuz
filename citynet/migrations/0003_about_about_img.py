# Generated by Django 3.0.7 on 2020-06-28 00:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('citynet', '0002_auto_20200627_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_img',
            field=models.ImageField(default=datetime.datetime(2020, 6, 28, 0, 11, 23, 864416, tzinfo=utc), upload_to='img/about'),
            preserve_default=False,
        ),
    ]