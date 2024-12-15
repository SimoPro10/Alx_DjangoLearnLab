from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_notifications, name='fetch-notifications'),
    path('<int:pk>/read/', views.mark_notification_as_read, name='mark-notification-read'),
]
