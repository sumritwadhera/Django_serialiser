import boto3

from opsec_app.s3_cost.serializers import cex

cost_s3=[]


def s3_monthly():
    ce = boto3.client('ce')
    cost = ce.get_cost_and_usage(
        TimePeriod={'Start': '2022-08-01', 'End': '2022-10-25'},
        Granularity = 'MONTHLY',
     Filter={
            'Dimensions': {
                'Key': 'SERVICE',
                'Values': ['Amazon Simple Storage Service'],

            }
        },
        Metrics=['UnblendedCost'],
        
        )
    print(cost)

    # for a in cost["ResultsByTime"]:
    #     print(a)
        # a["start_Date"]=a["TimePeriod"]["Start"]
        # a["End_Date"] = a["TimePeriod"]["End"]
        # a["Bill"] = a["Total"]["UnblendedCost"]["Amount"] + " USD"
        # print(a["Bill"])
    # print(a["End_Date"])


    #     ser = cex(data=a)
    #     if ser.is_valid():
    #         cost_s3.append(ser.data)
    #     else:
    #         print(ser.errors)
    # return cost_s3

    # print(cost_s3)

s3_monthly()






















# s3client = boto3.client('ce')
# response = s3client.get_cost_and_usage_with_resources(
#     TimePeriod={
#         'Start': '2022-12-03',
#         'End': '2022-12-09'
#     },
#     Granularity='MONTHLY',
#     Filter={
#         'Dimensions': {
#             'Key': 'SERVICE',
#             'Values': ['Simple Storage Service'],
#
#         }
#     },
#     Metrics=[
#         'NetAmortizedCost',
#     ],
# GroupBy=[
#         {
#             'Type': 'DIMENSION',
#             'Key': 'SERVICE'
#         }]
# )
