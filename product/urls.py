from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registerUserView, name='register'),
    

    path('', views.index, name='home'),
    path('create/', views.createProductView, name='create-product'),
    path('update/<str:pk>/', views.updateProductView, name='update-product'),
    path('delete/<str:pk>/', views.deleteProductView, name='delete-product'),

    path('cart/', views.addToCart, name='cart'),
    path('cart/', views.addToCart, name='cart')
]