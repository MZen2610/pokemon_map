# Generated by Django 3.1.7 on 2021-02-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20210222_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
