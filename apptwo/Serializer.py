from rest_framework import serializers
from .models import Rate, Signup, Rider, Passenger, MapVal, Image
from django import forms


class Items(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class Items1(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class IS(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = "__all__"


class IS1(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class IS2(serializers.ModelSerializer):
    class Meta:
        model = MapVal
        fields = "__all__"
