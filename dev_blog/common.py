from abc import ABC

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class BlogBaseSerializer(ModelSerializer):
    pass


class BaseQueryParamSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
