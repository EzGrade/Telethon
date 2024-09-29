from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon_auto_subsc.logger import get_logger
from django.conf import settings

import time

from .telethon_core import TelethonCore

logger = get_logger(__name__)


class ChannelsUtils:
    def __init__(self, account: TelethonCore = None, channels: list = None):
        self.account = account
        self.channels = channels or []

        self.session = str(settings.BASE_DIR.parent) + "/" + str(self.account.session)

    async def subscribe_channels(self, delay: int = 5):
        async with TelegramClient(self.session, self.account.api_id, self.account.api_hash) as client:
            channel_count = len(self.channels)
            subscribed_channels = 0
            for index, channel in enumerate(self.channels):
                try:
                    await client(JoinChannelRequest(channel))
                    if index + 1 < channel_count:
                        time.sleep(delay)

                    subscribed_channels += 1
                except Exception as e:
                    logger.error(f'Error while subscribing to channel {channel}: {e}')

            logger.info(f'Subscribed to {subscribed_channels} channels')
            return subscribed_channels

    async def send_message(self, message: str, delay: int = 5):
        async with TelegramClient(self.session, self.account.api_id, self.account.api_hash, device_model="iPhone 12 Pro") as client:
            for channel in self.channels:
                try:
                    await client.send_message(channel, message)
                    logger.info(f'Message sent to {channel}')
                    time.sleep(delay)
                except Exception as e:
                    logger.error(f'Error while sending message to {channel}: {e}')

            return True
