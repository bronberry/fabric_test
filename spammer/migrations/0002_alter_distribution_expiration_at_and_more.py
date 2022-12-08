# Generated by Django 4.1.4 on 2022-12-08 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spammer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distribution",
            name="expiration_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 9, 14, 47, 27, 386566, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время завершения рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="filter",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Фильтр клиента"
            ),
        ),
    ]