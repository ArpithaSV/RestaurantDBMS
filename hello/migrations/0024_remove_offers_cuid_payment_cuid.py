# Generated by Django 4.0.1 on 2022-03-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0023_offers_cuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='cuid',
        ),
        migrations.AddField(
            model_name='payment',
            name='cuid',
            field=models.CharField(default='', max_length=500),
        ),
    ]
