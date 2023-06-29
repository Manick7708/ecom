from django.contrib import admin
from .models import *

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['name','password','phone','email']
    
# @admin.register(PostFeed)
# class PostFeedAdmin(admin.ModelAdmin):
#     list_display=['user','description']

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display=['post','image']

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display=['post','user']

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['user','post','comment']

# @admin.register(ReplayComment)
# class ReplayCommentAdmin(admin.ModelAdmin):
#     list_display=['user','comment','replay_comment'] 

# @admin.register(ReplayCommentLike)
# class ReplayCommentLikeAdmin(admin.ModelAdmin):
#     list_display=['user','replay_like']

# @admin.register(PostCommentLike)
# class PostCommentLikeAdmin(admin.ModelAdmin):
#     list_display=['post','user']

# @admin.register(Share)
# class ShareAdmin(admin.ModelAdmin):
#     list_display=['post','user']

# @admin.register(Email)
# class EmailAdmin(admin.ModelAdmin):
#     list_display=['name','password','email']

# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display=['name','model','color','cm']
from import_export.admin import ImportExportModelAdmin
from .models import Catagory, Product, Cart
from .resources import CatagoryResource, ProductResource, CartResource

@admin.register(Catagory)
class CatagoryAdmin(ImportExportModelAdmin):
    resource_class = CatagoryResource
    list_display=['name', 'image', 'description', 'status', 'trending', 'created_at']

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display=['catagory', 'name', 'vendor', 'product_image', 'quantity', 'original_price', 'selling_price', 'description', 'status', 'trending', 'created_at']

@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    resource_class = CartResource
    list_display=['user', 'product', 'Product_qty', 'created_at']
