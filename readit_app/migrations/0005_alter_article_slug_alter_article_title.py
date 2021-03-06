# Generated by Django 4.0.5 on 2022-06-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readit_app', '0004_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
