from django.contrib import admin
from main import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ItemComponent)
class ItemComponentAdmin(admin.ModelAdmin):
    pass


class ItemFileInlineBaseAdmin(admin.StackedInline):
    pass


class ItemFilePdfInlineAdmin(ItemFileInlineBaseAdmin):
    model = models.ItemFilePdf


class ItemFileVideoInlineAdmin(ItemFileInlineBaseAdmin):
    model = models.ItemFileVideo


class ItemFileAudioInlineAdmin(ItemFileInlineBaseAdmin):
    model = models.ItemFileAudio


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemFilePdfInlineAdmin,
        ItemFileVideoInlineAdmin,
        ItemFileAudioInlineAdmin,
    ]
