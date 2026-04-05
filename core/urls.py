from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_record, name='create'),
    path('records/', views.list_records, name='list'),
    path('update/<int:id>/', views.update_record, name='update'),
]