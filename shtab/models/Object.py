from django.db import models

class Sortforpo(models.Model):
    category = models.CharField (max_length=50, blank=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'сортировка для ПО'
        verbose_name_plural = 'сортировка для ПО'

class Object(models.Model):
    kratknaim = models.CharField (max_length=255, verbose_name='краткое наименование')
    polnnaim = models.TextField (max_length=500, verbose_name='полное наименование')
    objectaip = models.TextField (max_length=500, blank=True, verbose_name='объект по АИП')
    numberobjectaip = models.PositiveSmallIntegerField (blank=True,null=True, verbose_name='№ АИП')
    sortforpo = models.ForeignKey(Sortforpo,on_delete=models.PROTECT, blank=True,null=True, verbose_name='сортировка для ПО')

    def __str__(self):
        return self.kratknaim

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'