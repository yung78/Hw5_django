import datetime
import pytz

from django.db import models


#  Для заполнения таблиц  python manage.py import_data
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=240, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Данные температуры')
    created_at = models.DateTimeField(default=datetime.datetime.now(pytz.timezone('Europe/Moscow')),
                                      verbose_name='Дата/время измерения')
    sens_picture = models.ImageField(default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ('sensor',)
