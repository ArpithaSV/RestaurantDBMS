# Generated by Django 4.0.1 on 2022-03-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0022_orders_cuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='cuid',
            field=models.CharField(default='', max_length=500),
        ),
    ]
