# Generated by Django 4.1.1 on 2022-09-30 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 13, 28, 59, 454273, tzinfo=datetime.timezone.utc), verbose_name='Дата/время измерения'),
        ),
    ]
