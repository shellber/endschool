# Generated by Django 2.1.5 on 2019-03-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0011_auto_20190308_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='root',
            new_name='root_comment',
        ),
    ]