from django.urls import path
from .import views
urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('home', views.home, name='home'),
    path('user_views', views.user_views, name='user_views'),
    path('user_login', views.user_login, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('products', views.products_add, name='products'),
    path('products_view', views.products_view, name='products_view'),
    path('products_edit/<int:id1>', views.products_edit, name='products_edit'),
    path('products_delete/<int:id1>', views.products_delete, name='products_delete'),
    path('', views.index, name='index'),
    path('home1', views.home1, name='home1'),
    path('user_view', views.user_view, name='user_view'),
    path('order/<int:pid>/<int:pr>', views.order, name='order'),
    path('admin_view', views.admin_view, name='admin_view'),
    path('approve/<int:oid>', views.approve, name='approve'),
    path('reject/<int:oid>', views.reject, name='reject'),
    path('order_view',views.order_view, name='order_view'),
    path('payment/<int:id>/<int:t>',views.make_payment,name='payment'),
    path('wishlist/<int:id>',views.wishlist,name='wishlist'),
    path('review/<int:id>', views.review,name='review'),
    path('logt',views.logt,name='logt'),


]