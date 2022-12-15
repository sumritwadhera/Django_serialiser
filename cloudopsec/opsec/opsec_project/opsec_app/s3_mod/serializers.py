from rest_framework import serializers


class k2s3(serializers.Serializer):
    bucket = serializers.CharField(
        required=False,
        allow_null=True
    )
    CreationDate = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    Number_of_objects = serializers.JSONField(
        required=False,
        allow_null=True
    )
    region = serializers.CharField(
        required=False,
        allow_null=True
    )
    State = serializers.CharField(
        required=False,
        allow_null=True
    )
    Web_hosting = serializers.CharField(
        required=False,
        allow_null=True
    )