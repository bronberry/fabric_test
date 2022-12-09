# Generated by Django 4.1.4 on 2022-12-08 14:53

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("spammer", "0003_alter_client_options_alter_distribution_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="telephone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                region="RU",
                unique=True,
                verbose_name="Номер мобильного телефона клиента",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="expiration_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 9, 14, 53, 9, 734017, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата и время завершения рассылки",
            ),
        ),
    ]
