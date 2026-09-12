from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'booking/tables', BookingViewSet, basename='booking')
urlpatterns = [
    path('', index, name='index'),
    path('menu/items/', MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('', include(router.urls)),
]