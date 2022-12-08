from rest_framework import serializers

from .models import Message, Client, Distribution


class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            "created_at",
            "status",
            "timezone",
        )


class ClientListSerializer(serializers.ModelSerializer):

    message_set = MessageListSerializer(many=True, required=False)

    class Meta:
        model = Client
        fields = (
            "telephone",
            "telephone_code",
            "tag",
            "timezone",
            "message_set",
        )


class DistributionSerializer(serializers.ModelSerializer):

    client_set = ClientListSerializer(many=True, required=False)
    message_set = MessageListSerializer(many=True, required=False)

    class Meta:
        model = Distribution
        fields = (
            "text",
            "filter",
            "created_at",
            "expiration_at",
            "client_set",
            "message_set",
        )
