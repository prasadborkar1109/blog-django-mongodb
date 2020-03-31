from django.contrib import admin

from dev_blog.models import Post, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'owner']

    class Meta:
        model = Blog
        fields = ['id', 'name', 'title', 'owner']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog_id', 'title', 'author', 'publish', 'status']

    class Meta:
        model = Post
        fields = ['id', 'blog_id', 'title', 'author', 'publish', 'status']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
