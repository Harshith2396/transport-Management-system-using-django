# Generated by Django 2.2.6 on 2019-12-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_assign'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='bus_no',
            field=models.CharField(default='123', max_length=10),
        ),
    ]
