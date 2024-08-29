from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('product/<int:pk>', views.product, name='product'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('category/<str:foo>/', views.category, name='category'),
    path('update_info/', views.update_info, name='update_info'),
    path('search/', views.search, name='search'),
    path('events/', views.events, name='events'),
    path('events/classes_children', views.classes_children, name='classes_children'),
    path('events/classes_teens', views.classes_teens, name='classes_teens'),
    path('events/classes_adults', views.classes_adults, name='classes_adults'),
]
