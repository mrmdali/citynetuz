# Generated by Django 3.0.7 on 2020-06-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citynet', '0007_footersocialtext_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=254)),
                ('author', models.CharField(max_length=254)),
            ],
        ),
    ]
