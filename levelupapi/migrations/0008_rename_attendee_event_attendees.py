# Generated by Django 3.2.9 on 2022-01-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0007_event_attendee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='attendee',
            new_name='attendees',
        ),
    ]
