from http import HTTPStatus
from typing import Any, Type

from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema

from spammer.models import Distribution, Client, Message
from spammer.serializers import (
    DistributionSerializer,
    ClientListSerializer,
    MessageListSerializer,
)


class SoloModelViewSet(GenericViewSet):
    def list(
        self, request: Request, *args: list[Any], **kwargs: dict[Any, Any]
    ) -> Response:
        queryset: Type[QuerySet] = self.get_queryset()
        serializer: Type[Serializer] = self.get_serializer(queryset.first())
        data: dict[str, Any] = serializer.data
        return Response(data=data, status=HTTPStatus.OK)


@extend_schema(tags=["Distribution Page"])
class DistributionViewSet(SoloModelViewSet):
    queryset = Distribution.objects.prefetch_related(
        "client_set",
        "message_set",
    )
    serializer_class = DistributionSerializer


@extend_schema(tags=["Client Page"])
class ClientListViewSet(SoloModelViewSet):
    queryset = Client.objects.prefetch_related(
        "message_set",
    )
    serializer_class = ClientListSerializer


@extend_schema(tags=["Message Page"])
class MessageListViewSet(SoloModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
