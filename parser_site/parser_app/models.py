from django.db import models

# вторичная модель
class PariMatch(models.Model):
    game = models.CharField(max_length=200, verbose_name='Матч')
    total = models.FloatField(null=True, blank=True, verbose_name='Тотал')
    more = models.FloatField(null=True, blank=True, verbose_name='Больше')
    less = models.FloatField(null=True, blank=True, verbose_name='Меньше')
    league = models.CharField(null=True, max_length=200, verbose_name='Лига')
    # связь 'Rubric' если первичная модель описано позже и Rubric если раньше
    #league = models.ForeignKey('League', null=True, on_delete=models.SET_NULL, verbose_name='Лига')
    #kindofsport = models.ForeignKey('KindOfSport', null=True, on_delete=models.SET_NULL, verbose_name='Вид спорта')

    class Meta:
        # название модели во множественном числе
        verbose_name_plural = 'Игры parimatch.ru'
        # название модели в единственном числе
        verbose_name = 'Игра parimatch.ru'
        # сортировака по умочанию
        #ordering = ['-total']

# Первичная модель
class League(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Лиги'
        verbose_name = 'Лига'
        ordering = ['name']

class KindOfSport(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Виды спорта'
        verbose_name = 'Вид спорта'
        ordering = ['name']
