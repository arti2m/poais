from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .Ispolnitel import Ispolnitel
from .Shtab import Shtab
from .Object import Object

from django.conf import settings

# Create your models here.

class Forpo(models.Model):
    stat = models.CharField(max_length=20, blank=True, verbose_name='для ПО')

    def __str__(self):
        return self.stat

    class Meta:
        verbose_name = 'для ПО'
        verbose_name_plural = 'для ПО'

class Statysisp(models.Model):
    stat = models.CharField(max_length=60, blank=True, verbose_name='статус исполнения')

    def __str__(self):
        return self.stat

    class Meta:
        verbose_name = 'статус исполнения'
        verbose_name_plural = 'статусы исполнения'

class Poruchenie(models.Model):
    shtab = models.ForeignKey(Shtab, on_delete=models.PROTECT, null=True, blank=True, verbose_name='штаб')
    numberpor = models.PositiveSmallIntegerField (blank=True,null=True, verbose_name='№')
    otv = models.ForeignKey(Ispolnitel, on_delete=models.PROTECT, null=True, blank=True, verbose_name='ответственный',related_name='tasks_as_otv')
    soisp = models.ManyToManyField(Ispolnitel, null=True, blank=True, verbose_name='соисполнитель', related_name='tasks_as_soisp')
    object = models.ForeignKey(Object, on_delete=models.PROTECT, null=True, blank=True, verbose_name='объект')
    por = models.TextField(verbose_name='поручение')
    srokisp = models.DateField (null=True, blank=True, verbose_name='срок исполнения')
    forpo = models.ForeignKey (Forpo, on_delete=models.PROTECT, blank=True,null=True, verbose_name='для ПО')
    statysisp = models.ForeignKey (Statysisp, on_delete=models.PROTECT, verbose_name='статус исполнения')
    dateisp = models.DateField (null=True, blank=True, verbose_name='дата исполнения')
    itogi = models.TextField(blank=True, verbose_name='итоги')
    otprzapr = models.TextField(blank=True, verbose_name='информация по направлению запросов')
    polzapr = models.TextField(blank=True, verbose_name='Информация по получению ответа на запрос')
    kratkopisisppor = models.TextField(blank=True, verbose_name='краткое описание исполнения поручения')
    anal = models.TextField(blank=True, verbose_name='аналитика ("архивные" комментарии)')
    otvotpo = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True, verbose_name='Ответственный от ПО',default=User)
    # otvotpo = models.ForeignKey(settings., on_delete=models.PROTECT, blank=True,null=True, verbose_name='ответственный от ПО')
    obiaz = models.BooleanField (default=False, verbose_name='Принятые обязательства')
    gpr = models.BooleanField (default=False, verbose_name='ГПР')
    factsrivsroka = models.BooleanField (default=False, verbose_name='Факты срыва срока')
    porneizprot = models.BooleanField (default=False, verbose_name='Поручения не из протокола')
    kritvopr = models.BooleanField (default=False, verbose_name='Критичный вопрос')
    redzone = models.BooleanField (default=False, verbose_name='Объект красной зоны')


    def __str__(self):
        return self.por

    def get_absolute_url(self):
        return reverse ('pordetaielview', kwargs = {'por_pk' : self.pk})

    class Meta:
        verbose_name = 'поручение'
        verbose_name_plural = 'поручения'
        ordering = ['shtab']