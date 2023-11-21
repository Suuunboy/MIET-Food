from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('main/', views.main, name='main'),
    path('register/', views.register_user, name='reg'),
    path('staff_main/', views.staff_main, name='staff_main'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('update_item/', views.updateItem, name='update_item')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
