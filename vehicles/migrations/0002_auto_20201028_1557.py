# Generated by Django 3.1.1 on 2020-10-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='hg',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='noX',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='so2',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='ghg',
            field=models.IntegerField(default='000'),
        ),
    ]
