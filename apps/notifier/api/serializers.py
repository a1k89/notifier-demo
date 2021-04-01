from rest_framework import serializers

from ..models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            'uid',
            'name',
            'body',
            'client_action',
            'icon',
        ]


