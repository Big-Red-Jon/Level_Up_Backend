# Generated by Django 3.2.9 on 2022-01-11 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_alter_event_organizer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='game',
            new_name='gameId',
        ),
    ]