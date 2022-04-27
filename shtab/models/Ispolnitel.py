from django.db import models

class Organization(models.Model):
    kratknaim = models.CharField (max_length=50,verbose_name='краткое наименование организации')
    polnnaim = models.CharField (max_length=255,verbose_name='полное наименование организации')
    mail1 = models.EmailField(max_length=254, null=True, blank=True,verbose_name='общая электронная почта')

    def __str__(self):
        return self.kratknaim

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'

class Ispolnitel(models.Model):
    surname = models.CharField (max_length=25, verbose_name='фамилия')
    name = models.CharField (max_length=16,verbose_name='имя')
    patronymic = models.CharField (max_length=16,verbose_name='отчество')
    dolzhnost = models.CharField (max_length=150,verbose_name='должность')
    org = models.ForeignKey(Organization,on_delete=models.PROTECT,verbose_name='Организация')
    mail1 = models.TextField(null=True, blank=True,verbose_name='электронная почта')


    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}. ({self.org})'

    class Meta:
        verbose_name = 'ответственный'
        verbose_name_plural = 'ответственные'