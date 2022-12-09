from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin import StackedInline
from solo.admin import SingletonModelAdmin

from spammer.models import Distribution, Client, Message


class MessageInline(StackedInline):
    model = Message
    extra = 0


class ClientInline(StackedInline):
    model = Client
    extra = 0


@admin.register(Distribution)
class DistributionListAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("text",)
    inlines = (
        ClientInline,
        MessageInline,
    )


@admin.register(Message)
class MessageListAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("created_at",)


@admin.register(Client)
class ClientListAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("telephone",)
