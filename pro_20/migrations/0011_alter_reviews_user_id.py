# Generated by Django 5.0.1 on 2024-04-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_20', '0010_alter_wishlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='User_id',
            field=models.CharField(max_length=100),
        ),
    ]
