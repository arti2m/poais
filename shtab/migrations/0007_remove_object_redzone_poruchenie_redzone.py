# Generated by Django 4.0.3 on 2022-04-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shtab', '0006_alter_poruchenie_otvotpo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='redzone',
        ),
        migrations.AddField(
            model_name='poruchenie',
            name='redzone',
            field=models.BooleanField(default=False, verbose_name='объект красной зоны'),
        ),
    ]