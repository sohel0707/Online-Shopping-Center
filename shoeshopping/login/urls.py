from django.urls import path
from . import views


urlpatterns = [
        path('', views.index,name='index'),
	path('login',views.login,name='login'),
	path('register',views.register,name='register'),
	path('contactus',views.contactus,name='contactus'),
	path('aboutus',views.aboutus,name='aboutus'),
	path('single-product/<int:id>',views.single,name='single'),
	path('confirmation',views.confirmation,name='confirmation'),
	path('checkout',views.checkout,name='checkout'),
	path('tracker',views.tracker,name='tracker'),
	path('category',views.category,name='category'),
	path('cart',views.cart,name='cart'),
	path('logout',views.logout,name='logout'),
]
