# Generated by Django 4.1.4 on 2022-12-08 14:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telephone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        region=None,
                        unique=True,
                        verbose_name="Номер мобильного телефона клиента",
                    ),
                ),
                (
                    "telephone_code",
                    models.IntegerField(
                        verbose_name="Код мобильного оператора клиента"
                    ),
                ),
                ("tag", models.CharField(max_length=10, verbose_name="Тег")),
                (
                    "timezone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Часовой пояс UTC"
                    ),
                ),
                ("order", models.PositiveIntegerField(verbose_name="Порядок")),
            ],
            options={
                "verbose_name": "Страница клиента",
                "verbose_name_plural": "Страница клиентов",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="Distribution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.CharField(max_length=300, verbose_name="Текст сообщения"),
                ),
                (
                    "filter",
                    models.CharField(max_length=100, verbose_name="Фильтр клиента"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время запуска рассылки"
                    ),
                ),
                (
                    "expiration_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022, 12, 9, 14, 42, 0, 827923, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="Дата и время завершения рассылки",
                    ),
                ),
                ("order", models.PositiveIntegerField(verbose_name="Порядок")),
            ],
            options={
                "verbose_name": "Страница рассылки",
                "verbose_name_plural": "Страница рассылок",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания сообщения"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(blank=True, verbose_name="Статус сообщения"),
                ),
                (
                    "timezone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Часовой пояс UTC"
                    ),
                ),
                ("order", models.PositiveIntegerField(verbose_name="Порядок")),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spammer.client",
                        verbose_name="ID Клиента",
                    ),
                ),
                (
                    "distribution_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spammer.distribution",
                        verbose_name="ID Рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Страница сообщения",
                "verbose_name_plural": "Страница сообщений",
                "ordering": ("order",),
            },
        ),
        migrations.AddField(
            model_name="client",
            name="distribution_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="spammer.distribution",
                verbose_name="Страница рассылки",
            ),
        ),
    ]
