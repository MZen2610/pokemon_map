# Generated by Django 3.1.7 on 2021-02-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
