from datetime import timedelta

from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Distribution(models.Model):
    """
    Модель рассылки
    """

    text = models.CharField(verbose_name="Текст сообщения", max_length=300)
    filter = models.CharField(verbose_name="Фильтр клиента", max_length=100, blank=True)
    created_at = models.DateTimeField(
        verbose_name="Дата и время запуска рассылки", auto_now_add=True, editable=False
    )
    expiration_at = models.DateTimeField(
        verbose_name="Дата и время завершения рассылки",
        default=timezone.now() + timedelta(days=1),
        editable=True,
    )
    order = models.PositiveIntegerField(verbose_name="Порядок")

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Рассылки"
        verbose_name_plural = "Рассылки"
        ordering = ("order",)


class Client(models.Model):
    """
    Модель клиента
    """

    telephone = PhoneNumberField(
        verbose_name="Номер мобильного телефона клиента",
        blank=True,
        unique=True,
        region="RU",
    )
    telephone_code = models.IntegerField(
        verbose_name="Код мобильного оператора клиента", blank=True
    )
    tag = models.CharField(verbose_name="Тег", max_length=10, blank=True)
    timezone = models.CharField(
        verbose_name="Часовой пояс UTC", blank=True, max_length=20
    )
    distribution_id = models.ForeignKey(
        verbose_name="Страница рассылки",
        to="spammer.Distribution",
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(verbose_name="Порядок")

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ("order",)


class Message(models.Model):
    """
    Модель сообщения
    """

    created_at = models.DateTimeField(
        verbose_name="Время создания сообщения", auto_now_add=True, editable=False
    )
    status = models.IntegerField(verbose_name="Статус сообщения", blank=True)
    timezone = models.CharField(
        verbose_name="Часовой пояс UTC", blank=True, max_length=20
    )
    client_id = models.ForeignKey(
        verbose_name="ID Клиента", to="spammer.Client", on_delete=models.CASCADE
    )
    distribution_id = models.ForeignKey(
        verbose_name="ID Рассылки", to="spammer.Distribution", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(verbose_name="Порядок")

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ("order",)
