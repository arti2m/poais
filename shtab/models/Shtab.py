from django.db import models


class Predsedatel(models.Model):
    predsedatel = models.CharField (max_length=15, blank=True, verbose_name='председатель')

    def __str__(self):
        return self.predsedatel

    class Meta:
        verbose_name = 'председатель штаба'
        verbose_name_plural = 'председатели штабов'

class Shtab(models.Model):
    dateshtabe = models.DateField (null=True, blank=True, verbose_name='дата проведения штаба')
    predsedatel = models.ForeignKey (Predsedatel, on_delete=models.PROTECT, blank=True, null=True, verbose_name='председатель штаба')


    def __str__(self):
        return f'{self.dateshtabe} {self.predsedatel}'


    class Meta:
        verbose_name = 'штаб'
        verbose_name_plural = 'штабы'