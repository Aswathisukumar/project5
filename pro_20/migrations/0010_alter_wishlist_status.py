# Generated by Django 5.0.1 on 2024-04-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_20', '0009_alter_wishlist_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='Status',
            field=models.CharField(max_length=100),
        ),
    ]