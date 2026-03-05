from django.urls import path
from . import views
from .auth_views import AdminLoginView, admin_logout

app_name = 'admin_dashboard'

urlpatterns = [
    path('', AdminLoginView.as_view(), name='login'),
    path('logout/', admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Posts URLs
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    
    # Categories URLs
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    
    # Messages URLs
    path('messages/', views.messages_list, name='messages_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('messages/<int:message_id>/delete/', views.message_delete, name='message_delete'),
    
    # Products URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
