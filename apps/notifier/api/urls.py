from django.urls import path

from .views import  NotificationListGenericApiView

urlpatterns = [
    path('', NotificationListGenericApiView.as_view())
]