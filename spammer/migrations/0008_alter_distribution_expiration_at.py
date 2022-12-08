# Generated by Django 4.1.4 on 2022-12-08 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spammer", "0007_alter_distribution_expiration_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distribution",
            name="expiration_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 9, 15, 43, 44, 791726, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время завершения рассылки",
            ),
        ),
    ]
