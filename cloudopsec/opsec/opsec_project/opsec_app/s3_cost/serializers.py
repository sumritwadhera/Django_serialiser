from rest_framework import serializers


class cex(serializers.Serializer):
    start_Date = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    End_Date = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    Region = serializers.CharField(
        required=False,
        allow_null=True
    )
    Bill = serializers.CharField(
        required=False,
        allow_null=True
    )
    # Number_of_objects = serializers.JSONField(
    #     required=False,
    #     allow_null=True
    # )

    # State = serializers.CharField(
    #     required=False,
    #     allow_null=True
    # )
    # Web_hosting = serializers.CharField(
    #     required=False,
    #     allow_null=True
    # )