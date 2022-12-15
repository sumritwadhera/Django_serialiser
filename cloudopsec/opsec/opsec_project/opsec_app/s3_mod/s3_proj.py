import boto3


from opsec_app.s3_mod.serializers import k2s3

bucket_details= []

def my_s3():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False)
    # print(regions)
    for i in regions['Regions']:
        k = (i['RegionName'])
        client = boto3.client('s3', region_name=k)
        response = client.list_buckets()
        for a in response['Buckets']:
            a['bucket'] = a['Name']
            a['region'] = i['RegionName']
            res = client.list_objects_v2(Bucket=a['Name'])
            a['Number_of_objects'] = res['KeyCount']
            # print(a)
            ser = k2s3(data=a)
            if ser.is_valid():
                bucket_details.append(ser.data)
            else:
                print(ser.errors)
        return bucket_details


# my_s3()



# import boto3
#
# from home.s3_bucket.serializers import k2s3
#
# bucket_details= []
#
# def my_s3():
#         client = boto3.client('s3')
#         response = client.list_buckets()
#         for a in response['Buckets']:
#             a['bucket'] = k
#             a['region'] = i['RegionName']
#
#
#             ser = k2s3(data=a)
#
#             if ser.is_valid():
#                 bucket_details.append(ser.data)
#             else:
#                 print(ser.errors)
#         return bucket_details
#
#
# my_s3()