import boto3
import json

from opsec_app.lamda.serializers import lam_ser

lam_details = []


def get():
    ec2client = boto3.client('ec2')
    response = ec2client.describe_regions(
        AllRegions=False
    )
    for i in response['Regions']:
        k = (i['RegionName'])

        session = boto3.session.Session(region_name=k)
        client = session.client('lambda')
        response = client.list_functions()
        if len(response['Functions']) > 0:
            a = response['Functions']

            for x in a:
                if 'VpcConfig' in x:
                    g = x['VpcConfig']
                    if len(g['SubnetIds']) > 0:
                        x['VpcConfig'] = g
                    else:
                        x['VpcConfig'] = False

                F = x['FunctionName']
                x['RegionName'] = k
                try:
                    session = boto3.session.Session()
                    client = session.client('lambda')
                    response2 = client.get_function_url_config(FunctionName=F)
                    y = response2['AuthType']
                    z = 'NONE'
                    if z in y:
                        x['is_Public'] = True
                except:
                    x['is_Public'] = False
                    x['RegionName'] = k
                ser = lam_ser(data=x)
                if ser.is_valid():
                    lam_details.append(ser.data)
                else:
                    print(ser.errors)

    return lam_details