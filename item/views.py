from django.shortcuts import render
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from item.models import Item
from item.serializers import ItemSerializer


class ItemViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Item.objects.filter(is_visible=True)
    serializer_class = ItemSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PageNumberPagination

