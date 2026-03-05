from django.contrib import admin
from .models import BlogPost, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at', 'categories']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'featured_image')
        }),
        ('Content', {
            'fields': ('content', 'excerpt')
        }),
        ('Publishing', {
            'fields': ('is_published', 'categories')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
