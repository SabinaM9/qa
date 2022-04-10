from rest_framework import serializers
from .models import TestResults


class AddResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = "__all__"


class ListResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = "__all__"
        # fields = {'test_date', 'squad', 'failed_tests'}
