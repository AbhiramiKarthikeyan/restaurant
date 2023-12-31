# Generated by Django 4.1.1 on 2023-03-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0028_customer_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_reviews',
            name='subject',
        ),
        migrations.AddField(
            model_name='add_specials',
            name='sstype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='add_blogs',
            name='blog',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='add_loc',
            name='lmap',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='feedback',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='customer_reviews',
            name='feedback',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant_feedback',
            name='feedback',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
