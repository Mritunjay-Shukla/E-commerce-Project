# Generated by Django 2.2.5 on 2020-07-08 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mstore', '0008_auto_20200708_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
