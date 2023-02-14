from rest_framework import serializers

from document.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('file', 'remark', 'uploaded_at')
