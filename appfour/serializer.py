from rest_framework import serializers
from .models import M


class Data(serializers.ModelSerializer):
    class Meta:
        model = M
        fields = "__all__"
