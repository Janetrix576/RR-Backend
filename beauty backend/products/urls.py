from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'reviews', views.ProductReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('featured/', views.FeaturedProductsView.as_view(), name='featured-products'),
    path('search/', views.ProductSearchView.as_view(), name='product-search'),
]
