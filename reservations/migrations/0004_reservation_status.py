# Generated by Django 5.1.6 on 2025-04-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_options_alter_room_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10),
        ),
    ]
