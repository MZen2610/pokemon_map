from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True,
                             verbose_name='Наименование')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/',
                              verbose_name='Картинка',
                              blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    title_en = models.CharField(max_length=200, blank=True,
                                verbose_name='Наименование анг.')
    title_jp = models.CharField(max_length=200, blank=True,
                                verbose_name='Наименование яп.')
    previous_evolution = models.ForeignKey("Pokemon",
                                           on_delete=models.SET_NULL,
                                           verbose_name='Из кого эволюционировал',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'
        ordering = ['title']


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey('Pokemon', on_delete=models.PROTECT,
                                verbose_name='Покемон', null=True, blank=True,
                                related_name='+')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True,
                                       verbose_name='Появился на')
    disappeared_at = models.DateTimeField(blank=True, null=True,
                                          verbose_name='Исчез в')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Атака')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True,
                                  verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon} широта = {self.lat} долгота = {self.lon}"

    class Meta:
        verbose_name = 'Характеристики покемона'
        verbose_name_plural = 'Характеристики покемонов'

