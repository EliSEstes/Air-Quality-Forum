# Generated by Django 3.1.1 on 2020-11-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20201113_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='wind',
        ),
        migrations.AddField(
            model_name='city',
            name='windDirection',
            field=models.IntegerField(default='000'),
        ),
    ]
