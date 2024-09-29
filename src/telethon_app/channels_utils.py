from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon_auto_subsc.logger import get_logger
from django.conf import settings

import asyncio
import random
import time

from .telethon_core import TelethonCore

logger = get_logger(__name__)


def randomize_delay(delay: int) -> float:
    random.seed(time.time())
    start = delay - 1 if delay - 1 > 0 else 0
    return random.uniform(start, delay + 2)


class ChannelsUtils:
    def __init__(self, account: TelethonCore = None, channels: list = None):
        self.account = account
        self.channels = channels or []

        self.session = str(settings.BASE_DIR.parent) + "/" + str(self.account.session)

    async def subscribe_channels(self, delay: int = 5):
        async with TelegramClient(self.session, self.account.api_id, self.account.api_hash) as client:
            channel_count = len(self.channels)
            for index, channel in enumerate(self.channels):
                try:
                    await client(JoinChannelRequest(channel))
                    logger.info(f'Subscribed to channel {channel}')
                except Exception as e:
                    logger.error(f'Error while subscribing to channel {channel}: {e}')
                finally:
                    channel_count -= 1
                    if channel_count > 1:
                        await asyncio.sleep(randomize_delay(delay))

                    if index % 10 == 0:
                        await asyncio.sleep(45)
            return True

    async def send_message(self, message: str, delay: int = 5):
        async with TelegramClient(self.session, self.account.api_id, self.account.api_hash) as client:
            channels_count = len(self.channels)
            for index, channel in enumerate(self.channels):
                try:
                    await client.send_message(channel, message)
                    logger.info(f'Message sent to {channel}')

                except Exception as e:
                    logger.error(f'Error while sending message to {channel}: {e}')
                finally:
                    channels_count -= 1
                    if channels_count > 1:
                        await asyncio.sleep(randomize_delay(delay))

                    if index % 10 == 0:
                        await asyncio.sleep(45)
            return True
