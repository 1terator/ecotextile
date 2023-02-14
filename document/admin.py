from django.contrib import admin

from document.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("remark", "is_visible")

    class Meta:
        model = Document
        exclude = []


admin.site.register(Document, DocumentAdmin)
