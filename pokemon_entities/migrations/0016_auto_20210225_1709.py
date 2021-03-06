# Generated by Django 3.1.7 on 2021-02-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20210224_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemonentity',
            options={'ordering': ['pk'], 'verbose_name': 'Характеристики покемона', 'verbose_name_plural': 'Характеристики покемонов'},
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='Наименование анг.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, verbose_name='Наименование яп.'),
        ),
    ]
