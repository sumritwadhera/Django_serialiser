from rest_framework import serializers


class cexit(serializers.Serializer):
    start_Date = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    End_Date = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    MONTH = serializers.CharField(
        required=False,
        allow_null=True
    )
    INSTANCE_TYPE = serializers.CharField(
        required=False,
        allow_null=True
    )
    Bill_FLOAT = serializers.FloatField(
        required=False,
        allow_null=True
    )
    Bill = serializers.CharField(
        required=False,
        allow_null=True
    )
