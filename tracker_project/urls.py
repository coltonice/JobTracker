from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from jobs import views

urlpatterns = [
    # Your custom auth views
    path('accounts/logout/', views.custom_logout_view, name='logout'),
    path('admin/', admin.site.urls),

    # Your other views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('add/', views.add_job, name='add_job'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]
