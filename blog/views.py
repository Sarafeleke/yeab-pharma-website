from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Category


def blog_list(request):
    """Blog list page with pagination and search"""
    posts = BlogPost.objects.filter(is_published=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(categories=category)
    
    # Pagination
    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for sidebar
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'current_category': category_slug,
    }
    return render(request, 'blog/blog_list.html', context)


def post_detail(request, slug):
    """Single blog post detail view"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Get related posts (same categories)
    related_posts = BlogPost.objects.filter(
        is_published=True,
        categories__in=post.categories.all()
    ).exclude(pk=post.pk).distinct()[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)
