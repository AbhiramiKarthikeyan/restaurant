# Generated by Django 4.1.1 on 2023-03-03 09:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurantapp', '0006_add_regs_delete_add_reg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_regs',
            new_name='add_photo',
        ),
    ]
