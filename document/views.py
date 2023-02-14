from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from document.models import Document
from document.serializers import DocumentSerializer


class DocumentViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Document.objects.filter(is_visible=True)
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PageNumberPagination
