from rest_framework import serializers
from .models import AppThree, PostAPI


class IS(serializers.ModelSerializer):
    class Meta:
        model = AppThree
        fields = "__all__"


class IS1(serializers.ModelSerializer):
    class Meta:
        model = PostAPI
        fields = "__all__"
