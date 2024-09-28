from django.db import models


# Create your models here.
class TelegramAccount(models.Model):
    telegram_id = models.PositiveBigIntegerField(blank=True, default=0)
    username = models.CharField(max_length=255, blank=True)
    api_id = models.CharField(max_length=255)
    api_hash = models.CharField(max_length=255)

    session_file = models.FileField(upload_to='sessions/')
    subscribed_channels = models.JSONField(blank=True, null=True, default=list)

    def __str__(self):
        return self.username
