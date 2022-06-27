# Generated by Django 4.0.5 on 2022-06-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kate', '0004_about_alter_profile_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('skills_count', models.IntegerField()),
                ('contact', models.EmailField(max_length=100)),
            ],
        ),
    ]
