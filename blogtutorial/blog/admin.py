from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
