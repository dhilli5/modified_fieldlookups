# Generated by Django 4.1.7 on 2023-04-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='name_of_game',
            new_name='gamen',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='player_name',
            new_name='playern',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name_of_game',
            new_name='gamen',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_name',
            new_name='playern',
        ),
    ]
