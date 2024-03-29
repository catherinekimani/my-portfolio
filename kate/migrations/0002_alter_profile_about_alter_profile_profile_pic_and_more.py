# Generated by Django 4.0.5 on 2022-06-26 17:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='resume'),
        ),
    ]
