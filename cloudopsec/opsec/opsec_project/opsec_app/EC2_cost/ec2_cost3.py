import boto3

from opsec_app.s3_cost.serializers import cex

cost_ec2=[]


def ec2_monthly():
    ce = boto3.client('ce')
    cost_com = ce.get_cost_and_usage(
        TimePeriod={'Start': '2022-08-01', 'End': '2022-10-25'},
        Granularity = 'MONTHLY',
     Filter={
            'Dimensions': {
                'Key': 'SERVICE',
                'Values': ['Amazon Elastic Compute Cloud - Compute'],
            },
        },
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION',
                  'Key': 'REGION',

                  } ,
                 {'Type': 'DIMENSION',
                  'Key': 'USAGE_TYPE',},
                 # {'Type': 'DIMENSION',
                 #  'Key': 'INSTANCE_TYPE', }

                 ]
    )

    print(cost_com)

ec2_monthly()