# Generated by Django 4.1.7 on 2023-04-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_playern_location_playerna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playern',
            field=models.CharField(max_length=100),
        ),
    ]