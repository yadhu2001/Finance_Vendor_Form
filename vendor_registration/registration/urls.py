from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.vendor_registration, name='vendor_registration'),
    path('vendor_list/', views.vendor_list),     path('export-vendors/', views.export_selected_vendors, name='export_selected_vendors'),
    path('success/', views.success_page, name='success_page'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Optional: add logout
    path('vendor-list/', views.vendor_list, name='vendor_list'),

]
