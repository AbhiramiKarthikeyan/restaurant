# Generated by Django 4.1.1 on 2023-03-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0029_remove_customer_reviews_subject_add_specials_sstype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_menu',
            name='availability',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='add_shefs',
        ),
    ]
