from rest_framework import serializers

from .models import TestResults


class AddResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = "__all__"
