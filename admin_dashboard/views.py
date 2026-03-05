from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count, Q
from blog.models import BlogPost as Post, Category
from core.models import ContactMessage, Product
from .forms import ProductForm
from datetime import datetime, timedelta
import json

def is_staff_user(user):
    return user.is_staff

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def dashboard(request):
    """Main dashboard view with statistics"""
    # Additional security check - ensure user is truly authenticated and staff
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_dashboard:login')
    
    # Get statistics
    total_posts = Post.objects.count()
    total_categories = Category.objects.count()
    total_users = User.objects.count()
    total_messages = ContactMessage.objects.count()
    total_products = Product.objects.count()
    
    # Recent posts
    recent_posts = Post.objects.order_by('-created_at')[:5]
    
    # Recent messages
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    
    # Posts created in last 7 days
    seven_days_ago = datetime.now() - timedelta(days=7)
    recent_posts_count = Post.objects.filter(created_at__gte=seven_days_ago).count()
    
    context = {
        'total_posts': total_posts,
        'total_categories': total_categories,
        'total_users': total_users,
        'total_messages': total_messages,
        'total_products': total_products,
        'recent_posts': recent_posts,
        'recent_messages': recent_messages,
        'recent_posts_count': recent_posts_count,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def posts_list(request):
    """List all blog posts"""
    # Additional security check
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_dashboard:login')
    posts = Post.objects.all().order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    
    return render(request, 'admin_dashboard/posts_list.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def post_create(request):
    """Create a new blog post"""
    # Additional security check
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_dashboard:login')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt', '')
        status = request.POST.get('status', 'draft')
        featured_image = request.FILES.get('featured_image')
        category_ids = request.POST.getlist('categories')
        
        if title and content:
            post = Post.objects.create(
                title=title,
                content=content,
                excerpt=excerpt,
                featured_image=featured_image,
                author=request.user
            )
            
            # Set published status
            if status == 'published':
                post.is_published = True
            post.save()
            
            # Add categories
            if category_ids:
                post.categories.set(category_ids)
            
            messages.success(request, 'Post created successfully!')
            return redirect('admin_dashboard:posts_list')
        else:
            messages.error(request, 'Title and content are required!')
    
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'admin_dashboard/post_form.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def post_edit(request, post_id):
    """Edit an existing blog post"""
    # Additional security check
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_dashboard:login')
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt', '')
        status = request.POST.get('status', 'draft')
        featured_image = request.FILES.get('featured_image')
        category_ids = request.POST.getlist('categories')
        
        if title and content:
            post.title = title
            post.content = content
            post.excerpt = excerpt
            
            if featured_image:
                post.featured_image = featured_image
            
            # Set published status
            post.is_published = (status == 'published')
            post.save()
            
            # Update categories
            if category_ids:
                post.categories.set(category_ids)
            
            messages.success(request, 'Post updated successfully!')
            return redirect('admin_dashboard:posts_list')
        else:
            messages.error(request, 'Title and content are required!')
    
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'admin_dashboard/post_form.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def post_delete(request, post_id):
    """Delete a blog post"""
    print(f"DEBUG: Delete view called - post_id: {post_id}, method: {request.method}")
    
    post = get_object_or_404(Post, id=post_id)
    print(f"DEBUG: Found post: {post.title}")
    
    if request.method == 'POST':
        print("DEBUG: POST request - deleting post")
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('admin_dashboard:posts_list')
    
    print("DEBUG: GET request - rendering delete template")
    context = {'post': post}
    return render(request, 'admin_dashboard/post_delete.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def categories_list(request):
    """List all categories"""
    categories = Category.objects.all().annotate(post_count=Count('posts'))
    
    context = {'categories': categories}
    return render(request, 'admin_dashboard/categories_list.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def category_create(request):
    """Create a new category"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        slug = request.POST.get('slug', '')
        
        if name:
            category = Category.objects.create(
                name=name,
                description=description,
                slug=slug or name.lower().replace(' ', '-')
            )
            messages.success(request, 'Category created successfully!')
            return redirect('admin_dashboard:categories_list')
        else:
            messages.error(request, 'Name is required!')
    
    return render(request, 'admin_dashboard/category_form.html')

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def category_edit(request, category_id):
    """Edit an existing category"""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        slug = request.POST.get('slug', '')
        
        if name:
            category.name = name
            category.description = description
            category.slug = slug or name.lower().replace(' ', '-')
            category.save()
            
            messages.success(request, 'Category updated successfully!')
            return redirect('admin_dashboard:categories_list')
        else:
            messages.error(request, 'Name is required!')
    
    context = {'category': category}
    return render(request, 'admin_dashboard/category_form.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def category_delete(request, category_id):
    """Delete a category"""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('admin_dashboard:categories_list')
    
    context = {'category': category}
    return render(request, 'admin_dashboard/category_delete.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def messages_list(request):
    """List all contact messages"""
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    
    # Mark as read functionality
    message_id = request.GET.get('mark_read')
    if message_id:
        message = get_object_or_404(ContactMessage, id=message_id)
        message.is_read = True
        message.save()
        return redirect('admin_dashboard:messages_list')
    
    # Pagination
    paginator = Paginator(messages_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    return render(request, 'admin_dashboard/messages_list.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def message_detail(request, message_id):
    """View message details"""
    message = get_object_or_404(ContactMessage, id=message_id)
    
    # Mark as read
    if not message.is_read:
        message.is_read = True
        message.save()
    
    context = {'message': message}
    return render(request, 'admin_dashboard/message_detail.html', context)

@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def message_delete(request, message_id):
    """Delete a message"""
    message = get_object_or_404(ContactMessage, id=message_id)
    
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('admin_dashboard:messages_list')
    
    context = {'message': message}
    return render(request, 'admin_dashboard/message_delete.html', context)


# Product Views
@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def product_list(request):
    """List all products"""
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    return render(request, 'admin_dashboard/product_list.html', context)


@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def product_create(request):
    """Create a new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('admin_dashboard:product_list')
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'admin_dashboard/product_form.html', context)


@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def product_edit(request, product_id):
    """Edit an existing product"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('admin_dashboard:product_list')
    else:
        form = ProductForm(instance=product)
    
    context = {'form': form, 'product': product}
    return render(request, 'admin_dashboard/product_form.html', context)


@login_required(login_url='admin_dashboard:login')
@user_passes_test(is_staff_user, login_url='admin_dashboard:login')
def product_delete(request, product_id):
    """Delete a product"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('admin_dashboard:product_list')
    
    context = {'product': product}
    return render(request, 'admin_dashboard/product_delete.html', context)
