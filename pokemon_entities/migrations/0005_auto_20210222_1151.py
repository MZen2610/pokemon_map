# Generated by Django 3.1.7 on 2021-02-22 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20210222_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lon',
            new_name='lon',
        ),
    ]
