from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework import routers

# routers = routers.DefaultRouter()
# routers.register('', UserViewSet)

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', getRouters, name='Routers'),
    path('products/', getProducts, name='products'),
    path('products/<str:pk>', getProduct, name='product'),
    path('users/profile/', getUserProfile, name='userProfile'),
    path('users/', getUsers, name='getUsers'),
    path('users/register/', registerUser, name='register'),
    path('users/profile/update/', updateUserProfile, name='updateUserProfile'),
    path('order/add/', addOrderItems, name='order_add'),
    path('order/<int:pk>/', getOrderById, name='getOrderById'),
    path('order/<int:pk>/pay/', updateOrderToPaid, name='update_paid'),
    path('order/myorders/', getMyOrder, name='myOrder'),
    path('delete/<int:pk>/', deleteuser, name='delete_user'),
    path('user/update/<int:pk>/', updateUser, name='update-user'),
    path('user/<int:pk>/', getUserById, name='getUserById'),
    path('product/delete/<int:pk>/', deleteProduct, name='delete-product'),
    path('product/create/', createProduct, name='create_Product'),
    path('product/update/<int:pk>/', updateProduct, name='product_Update'),
    path('product/upload/', uploadImage, name='upload_Image'),
    path('order/', getOrders, name='get_orders'),
    path('order/<int:pk>/deliver/', updateOrderToDelivered, name='update_delivered'),

]
