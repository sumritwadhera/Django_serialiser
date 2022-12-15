from rest_framework import serializers


class lam_ser(serializers.Serializer):
    FunctionName = serializers.CharField(
        required=False,
        allow_null=True
    )
    FunctionArn = serializers.CharField(
        required=False,
        allow_null=True
    )
    Runtime = serializers.CharField(
        required=False,
        allow_null=True
    )
    RegionName = serializers.CharField(
        required=False,
        allow_null=True
    )
    is_Public = serializers.BooleanField(
        required=False,
        allow_null=True,
        default=False,
        )