# Generated by Django 3.1.1 on 2020-11-13 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20201113_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='n',
            new_name='no2',
        ),
    ]