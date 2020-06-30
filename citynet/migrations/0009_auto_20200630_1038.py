# Generated by Django 3.0.7 on 2020-06-30 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('citynet', '0008_footerauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffabout',
            name='tariff_header_first',
            field=models.CharField(default=-1.0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tariffabout',
            name='tariff_header_second',
            field=models.CharField(default=datetime.datetime(2020, 6, 30, 5, 38, 8, 325636, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tariffabout',
            name='tariff_header_third',
            field=models.CharField(default=datetime.datetime(2020, 6, 30, 5, 38, 46, 110642, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='about_second_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_third_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]