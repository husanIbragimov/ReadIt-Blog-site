# Generated by Django 4.0.5 on 2022-06-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
