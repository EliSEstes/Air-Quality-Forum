# Generated by Django 3.1.1 on 2020-10-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='?', max_length=100)),
                ('model', models.CharField(default='?', max_length=100)),
                ('co2', models.IntegerField(default='000')),
                ('so2', models.IntegerField(default='000')),
                ('noX', models.IntegerField(default='000')),
                ('hg', models.IntegerField(default='000')),
            ],
        ),
    ]
