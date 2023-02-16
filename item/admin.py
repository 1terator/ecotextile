from django.contrib import admin

from item.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at", "price", "is_visible")

    class Meta:
        model = Item
        exclude = []


admin.site.register(Item, ItemAdmin)
