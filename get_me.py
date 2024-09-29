from telethon import TelegramClient


async def get_me(session, api_id, api_hash):
    async with TelegramClient(session, api_id, api_hash) as client:
        me = await client.get_me()
        return me


if __name__ == "__main__":
    import asyncio

    api_id = 24513991
    api_hash = "565f76ce73fc3eac832ebbbe0ce79339"
    session = "/home/grade/Downloads/12222224_telethon.session"

    me = asyncio.run(get_me(session, api_id, api_hash))
    print(me)
