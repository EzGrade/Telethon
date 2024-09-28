from django.contrib import admin
from .models import TelegramAccount


# Register your models here.
@admin.register(TelegramAccount)
class TelegramAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'api_id', 'api_hash')
