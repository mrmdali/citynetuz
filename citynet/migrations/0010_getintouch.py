# Generated by Django 3.0.7 on 2020-06-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citynet', '0009_auto_20200630_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('message_subject', models.CharField(max_length=100)),
                ('message_text', models.TextField()),
                ('read_or_not', models.BooleanField(default=False)),
            ],
        ),
    ]