from rest_framework import generics

from .serializers import NotificationSerializer
from ..models import Notification


class NotificationListGenericApiView(generics.ListAPIView):
    """
    Get a list of notifications for a current user with pagination. Readonly

    """
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification\
            .actions\
            .for_user(self.request.user)
