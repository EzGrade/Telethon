import asyncio

from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import TelegramAccount
from .serializers import TelegramAccountSerializer, SubscribeChannelsSerializer
from .channels_utils import ChannelsUtils
from telethon_auto_subsc.logger import get_logger

from .telethon_core import TelethonCore

logger = get_logger(__name__)


class TelegramAccountViewSet(ModelViewSet):
    queryset = TelegramAccount.objects.all()
    serializer_class = TelegramAccountSerializer


class SubscribeChannelsViewSet(ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_summary='Subscribe to channels',
        request_body=SubscribeChannelsSerializer,
        responses={200: 'ok'}
    )
    def create(self, request):
        dataclasses = SubscribeChannelsSerializer(data=request.data)
        dataclasses.is_valid(raise_exception=True)

        if not dataclasses.is_valid():
            logger.error(dataclasses.errors)
            return Response(dataclasses.errors, status=400)

        data = dataclasses.validated_data
        data_accounts = data['telegram_accounts']
        data_channels = data['channels'].read().decode('utf-8').splitlines()
        delay = data.get('delay', 5)

        logger.info(f'Accounts: {data_accounts}')
        logger.info(f'Channels: {data_channels}')

        accounts_qs = TelegramAccount.objects.filter(telegram_id__in=data_accounts)
        processing_sessions = set()
        for account in accounts_qs:
            if account.session_file in processing_sessions:
                continue
            account_object = TelethonCore(
                api_id=account.api_id,
                api_hash=account.api_hash,
                session=account.session_file
            )
            processing_sessions.add(account.session_file)
            utils = ChannelsUtils(account_object, data_channels)
            asyncio.run(utils.subscribe_channels(delay))

        return Response({'status': 'ok'})


class SendMessageViewSet(ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_summary='Send message to channels',
        request_body=SubscribeChannelsSerializer,
        responses={200: 'ok'}
    )
    def create(self, request):
        dataclasses = SubscribeChannelsSerializer(data=request.data)
        if not dataclasses.is_valid():
            return Response(dataclasses.errors, status=400)

        data = dataclasses.validated_data
        data_accounts = data['telegram_accounts']
        data_channels = data['channels'].read().decode('utf-8').splitlines()
        data_delay = data.get('delay', 5)
        data_message = data['message']

        logger.info(f'Accounts: {data_accounts}')
        logger.info(f'Channels: {data_channels}')

        accounts_qs = TelegramAccount.objects.filter(telegram_id__in=data_accounts)
        for account in accounts_qs:
            account_object = TelethonCore(
                api_id=account.api_id,
                api_hash=account.api_hash,
                session=account.session_file
            )
            utils = ChannelsUtils(account_object, data_channels)
            asyncio.run(utils.send_message(data_message, data_delay))

        return Response({'status': 'ok'})
