from django.contrib import admin
from .models import *


class CateAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "created", "updated"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "created", "updated"]


class BlogAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "author", "cate", "desc", "cat", "created", "updated"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "ip", "blog", "content", "created", "updated"]


admin.site.register(Cate, CateAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
