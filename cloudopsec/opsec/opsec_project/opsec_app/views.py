from rest_framework.response import Response
from rest_framework.views import APIView

from opsec_app.EC2_cost_User_type.EC2_usage import ec2_US
from opsec_app.EC2_cost_instance_type.EC2_instancetype import ec2_IT
from opsec_app.EC2_cost_other.EC2_other import ec2_OTU
from opsec_app.EC2_cost_other_region.EC2_other_region import ec2_RG1
from opsec_app.EC2_cost_region.EC2_region import ec2_RG
from opsec_app.lamda.lamda import get
from opsec_app.s3_cost.cost import s3_monthly
from opsec_app.s3_mod.s3_proj import my_s3


class S3(APIView):
    @staticmethod
    def post(self):
        S3 = my_s3()
        return Response(S3)

class Lambda2(APIView):
    @staticmethod
    def post(self):
        lambda2 = get()
        return Response(lambda2)

class cost3(APIView):
    @staticmethod
    def post(self):
        cost3 = s3_monthly()
        return Response(cost3)

class ITYPE(APIView):
    @staticmethod
    def post(self):
        ITYPE = ec2_IT()
        return Response(ITYPE)

class USTYPE(APIView):
    @staticmethod
    def post(self):
        USTYPE = ec2_US()
        return Response(USTYPE)

class REG(APIView):
    @staticmethod
    def post(self):
        REG = ec2_RG()
        return Response(REG)

class USAGE(APIView):
    @staticmethod
    def post(self):
        USAGE = ec2_OTU()
        return Response(USAGE)

class REG_OT(APIView):
    @staticmethod
    def post(self):
        REG_OT = ec2_RG1()
        return Response(REG_OT)