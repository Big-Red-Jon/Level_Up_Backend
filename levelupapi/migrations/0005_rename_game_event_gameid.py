# Generated by Django 3.2.9 on 2022-01-11 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_rename_gameid_event_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='game',
            new_name='gameId',
        ),
    ]
