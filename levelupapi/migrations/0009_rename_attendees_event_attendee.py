# Generated by Django 3.2.9 on 2022-01-16 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0008_rename_attendee_event_attendees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='attendees',
            new_name='attendee',
        ),
    ]