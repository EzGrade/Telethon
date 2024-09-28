import asyncio

from telethon import TelegramClient
from telethon.tl.types import User


class TelethonCore:
    def __init__(self, api_id: str, api_hash: str, session: str) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.session = session
        self.client = None

    async def connect_telethon_client(self) -> None:
        self.client = TelegramClient(self.session, self.api_id, self.api_hash)
        await self.client.start()

    def get_active_client(self) -> TelegramClient:
        return asyncio.run(self.connect_telethon_client())

    async def get_user(self) -> User:
        if not self.client:
            await self.connect_telethon_client()
        user = await self.client.get_me()
        return user
