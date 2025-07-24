from django.contrib import admin
from .models import Category, Brand, Product, ProductImage, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'stock_quantity', 'is_active', 'is_featured']
    list_filter = ['category', 'brand', 'is_active', 'is_featured', 'created_at']
    search_fields = ['name', 'sku', 'description']
    inlines = [ProductImageInline]
    
    def save_model(self, request, obj, form, change):
        if not obj.sku:
            # Generate SKU automatically
            obj.sku = f"{obj.brand.name[:3].upper()}-{obj.name[:3].upper()}-{obj.id or '001'}"
        super().save_model(request, obj, form, change)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    actions = ['approve_reviews', 'reject_reviews']
    
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    
    def reject_reviews(self, request, queryset):
        queryset.update(is_approved=False)
