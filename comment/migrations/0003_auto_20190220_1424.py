# Generated by Django 2.1.5 on 2019-02-20 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190220_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]