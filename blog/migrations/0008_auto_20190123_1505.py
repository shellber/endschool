# Generated by Django 2.1.5 on 2019-01-23 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190123_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='blog',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]
