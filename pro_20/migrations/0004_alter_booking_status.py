# Generated by Django 5.0.1 on 2024-03-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_20', '0003_alter_booking_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Status',
            field=models.CharField(max_length=100),
        ),
    ]
