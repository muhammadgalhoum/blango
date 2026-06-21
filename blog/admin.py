from django.contrib import admin
from blog.models import Tag, Post, Comment


admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published_at"]
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Comment)