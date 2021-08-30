from django.contrib import admin
from .models import Price, News


class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')


admin.site.register(Price, PriceAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'link')


admin.site.register(News, NewsAdmin)
