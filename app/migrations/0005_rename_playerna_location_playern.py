# Generated by Django 4.1.7 on 2023-04-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_player_playern'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='playerna',
            new_name='playern',
        ),
    ]
