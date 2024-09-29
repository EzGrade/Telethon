from rest_framework import serializers

from .models import TelegramAccount


class TelegramAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramAccount
        fields = '__all__'


class SubscribeChannelsSerializer(serializers.Serializer):
    telegram_accounts = serializers.ListField(
        child=serializers.IntegerField()
    )
    channels = serializers.FileField()
    message = serializers.CharField(required=False)
    delay = serializers.IntegerField(required=False)
