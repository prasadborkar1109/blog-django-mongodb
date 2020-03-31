from rest_framework import serializers

from dev_blog.common import BlogBaseSerializer, BaseQueryParamSerializer
from dev_blog.models import Blog, Post


class BlogSerializer(BlogBaseSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'title', 'owner']


class PostSerializer(BlogBaseSerializer):

    class QueryParamSerializer(BaseQueryParamSerializer):
        blog = serializers.IntegerField(required=False)
        publish_status = serializers.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'blog_id', 'title', 'author', 'publish', 'status']

    param_serializer = QueryParamSerializer
