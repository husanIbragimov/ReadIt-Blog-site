# Generated by Django 4.0.5 on 2022-06-08 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readit_app', '0011_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
