from telethon import TelegramClient
import asyncio


async def get_session() -> TelegramClient:
    api_id = '27335138'
    api_hash = '2459555ba95421148c682e2dc3031bb6'
    session = 'anonoymous'
    async with TelegramClient(session, api_id, api_hash) as client:
        return await client.get_me()


if __name__ == '__main__':
    client = asyncio.run(get_session())
    print(client)
