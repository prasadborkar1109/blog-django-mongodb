from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from dev_blog.serializers import BlogSerializer, PostSerializer
from dev_blog.models import Blog, Post


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='Get List of Blogs'))
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        return self.queryset


@method_decorator(name='list', decorator=swagger_auto_schema(query_serializer=PostSerializer.param_serializer))
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    param_serializer = PostSerializer.param_serializer

    def get_queryset(self):
        query_params = self.request.query_params.copy()
        print(query_params)
        if 'publish_status' in query_params:
            query_params['publish_status'] = 'published' if query_params['publish_status'] == 'true' else 'draft'
        param_dict = {'user': 'author', 'blog': 'blog_id',
                      'publish_status': 'status'}
        filters = {}
        for key, value in query_params.items():
            if key in param_dict:
                filters[param_dict.get(key)] = value

        return self.queryset.filter(**filters)
