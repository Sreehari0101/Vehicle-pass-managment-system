# Generated by Django 4.2.1 on 2023-05-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_booking_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='registration_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
