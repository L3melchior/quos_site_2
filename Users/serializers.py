from rest_framework import serializers
from Users.models import RequestQR

class RequestQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestQR
        fields = "__all__"

