from django.urls import path
from . import views

urlpatterns = [
    path('admin_page/',views.admin_page,name='admin_page'),
    path('add_product/', views.add_product, name='add_product'),
    path('products_list/', views.products_list, name='products_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/<str:active>/', views.delete_product, name='delete_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('category_list/', views.category_list, name='category_list'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('user/', views.user, name='user'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('order_views/<int:order_id>/',views.order_views,name='order_views'),
    path('order_all/', views.order_all, name='order_all'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('add_variant/<int:product_id>/', views.add_variant, name='add_variant'),
    path('variant_edit/<int:variant_id>/', views.variant_edit, name='variant_edit'),
    path('enable_product/<int:product_id>/', views.enable_product, name='enable_product'),
    path('disable_product/<int:product_id>/', views.disable_product, name='disable_product'),
    path('product_view/<int:product_id>/', views.product_view, name='product_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pdf_view/', views.pdf_view, name='pdf_view'),
    path('download_order_pdf_sales/', views.download_order_pdf_sales, name='download_order_pdf_sales'),
    path('view_coupon/', views.view_coupon, name='view_coupon'),
    path('add_coupon/', views.add_coupon, name='add_coupon'),
    path('edit_coupon/<int:coupon_id>/', views.edit_coupon, name='edit_coupon'),
    path('disable_coupon/<int:coupon_id>/', views.disable_coupon, name='disable_coupon' ),
    path('enable_coupon/<int:coupon_id>/', views.enable_coupon, name='enable_coupon' ),
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('order_shipped/<int:order_id>', views.order_shipped, name='order_shipped'),
    path('admin_order_cancel/<int:order_id>', views.admin_order_cancel, name='admin_order_cancel'),
    path('order_deliverd/<int:order_id>', views.order_deliverd, name='order_deliverd'),
    
    
    

]
# path('products/', views.products, name='products'),
# path('products/detail/<int:pk>/', views.product_detail,name='products-detail'),
# path('admin/category/add/', views.add_category, name='add_category'),