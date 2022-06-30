# Generated by Django 4.0.5 on 2022-06-27 07:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kate', '0005_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('project_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
