# Generated by Django 4.1.1 on 2023-03-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0013_remove_add_photo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_photo',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.restaurant_reg'),
        ),
    ]
