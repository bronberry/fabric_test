# Generated by Django 4.1.4 on 2022-12-09 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spammer', '0009_alter_distribution_expiration_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='expiration_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 13, 36, 50, 619692, tzinfo=datetime.timezone.utc), verbose_name='Дата и время завершения рассылки'),
        ),
    ]
