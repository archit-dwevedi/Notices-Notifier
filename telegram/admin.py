from django.contrib import admin

# Register your models here.
from .models import telegram_id,telegram_offset




admin.site.register(telegram_id)
admin.site.register(telegram_offset)
