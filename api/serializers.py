from rest_framework import serializers
from apptwo.models import Rate


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"
