# Generated by Django 4.0.5 on 2022-06-30 05:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kate', '0006_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('contact_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.EmailField(max_length=100)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]
