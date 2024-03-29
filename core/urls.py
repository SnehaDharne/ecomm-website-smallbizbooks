from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    PolBookStoreView,
    TatBookStoreView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    AddCouponView,
    SearchResultsView
)
from . import views

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Politics/', TatBookStoreView, name='tat'),
    path('Mystery/', PolBookStoreView, name='pol'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path("search/", SearchResultsView.as_view(), name='search_results'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
