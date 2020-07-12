# Generated by Django 2.2.5 on 2020-07-02 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mstore', '0003_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='mstore.Cart'),
            preserve_default=False,
        ),
    ]
