# Generated by Django 4.1.1 on 2023-03-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0025_delete_add_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_reg',
            name='payment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
