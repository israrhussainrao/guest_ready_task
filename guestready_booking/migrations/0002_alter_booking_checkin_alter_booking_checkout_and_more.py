# Generated by Django 5.1.1 on 2024-09-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestready_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flat',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
