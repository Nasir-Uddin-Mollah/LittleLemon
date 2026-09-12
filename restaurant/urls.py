from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'booking/tables', BookingViewSet, basename='booking')
urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('menu/items/', MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]