from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('history/', views.leave_history, name='leave_history'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update/<int:leave_id>/<str:action>/', views.update_leave_status, name='update_leave_status'),
]
