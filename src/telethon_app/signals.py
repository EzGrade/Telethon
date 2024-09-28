import os

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import TelegramAccount
from .telethon_core import TelethonCore
import asyncio


@receiver(post_save, sender=TelegramAccount)
def create_telegram_account(sender, instance, created, **kwargs):
    if created:
        client = TelethonCore(
            api_id=instance.api_id,
            api_hash=instance.api_hash,
            session=instance.session_file.name
        )

        user = asyncio.run(client.get_user())
        instance.username = user.username
        instance.telegram_id = user.id

        session_name = f'sessions/{user.id}.session'
        os.rename(instance.session_file.path, session_name)
        instance.session_file.name = session_name

        instance.save()


@receiver(post_delete, sender=TelegramAccount)
def delete_telegram_account(sender, instance, **kwargs):
    if instance.session_file:
        instance.session_file.delete(save=False)
