# Generated by Django 2.2.4 on 2019-10-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191005_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='studs',
            name='email',
            field=models.EmailField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='studs',
            name='phone',
            field=models.CharField(default='NA', max_length=10),
        ),
    ]
