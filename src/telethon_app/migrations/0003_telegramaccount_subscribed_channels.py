# Generated by Django 5.1.1 on 2024-09-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telethon_app', '0002_remove_telegramaccount_subscribed_channels'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramaccount',
            name='subscribed_channels',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
