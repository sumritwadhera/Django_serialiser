import decimal

import boto3

from opsec_app.EC2_cost_instance_type.serializers import cexit


cost_IT=[]


def ec2_IT():
    ce = boto3.client('ce')
    cost_com = ce.get_cost_and_usage(
        TimePeriod={'Start': '2022-08-01', 'End': '2022-10-25'},
        Granularity = 'MONTHLY',
     Filter={ "And": [ {"Dimensions": { "Key": "SERVICE", "Values": ["Amazon Elastic Compute Cloud - Compute"] }}, {"Not": {"Dimensions": { "Key": "RECORD_TYPE", "Values": ["Credit"] }}} ] }

            # 'Dimensions': {
            #     'Key': 'SERVICE',
            #     'Values': ['Amazon Elastic Compute Cloud - Compute'],
            # },
        ,
        Metrics=['UnblendedCost'],
        GroupBy=[
                 {'Type': 'DIMENSION',
                  'Key': 'INSTANCE_TYPE',}

                 ]
    )
    # print(cost_com)
    for a in cost_com["ResultsByTime"]:
        # print(a)
        a["start_Date"]=a["TimePeriod"]["Start"]
        a["End_Date"] = a["TimePeriod"]["End"]
        # Extracting month from start date
        d1 = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July",
              "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

        xr1 = a["start_Date"]
        xr2 = xr1.split("-")
        xr3 = xr2.pop(1)
        dt = d1[xr3]
        # print(dt)
        a["MONTH"] = dt
        # print(a["MONTH"])
        ####################################################
        for b in a["Groups"]:
            # print(b)
            reg=b["Keys"]
            sentence = " ".join(map(str, reg))
            a["INSTANCE_TYPE"]=sentence
            # print(a["INSTANCE_TYPE"])
            amount = b["Metrics"]["UnblendedCost"]["Amount"]
            a1 = decimal.Decimal(amount)
            val1 = round(a1, 5)
            val2 = str(val1)
            val3 = float(val2)
            a["Bill_FLOAT"] = val3
            a["Bill"] = val2 + " USD"
            # print(a["Bill"])
            ser = cexit(data=a)
            if ser.is_valid():
                cost_IT.append(ser.data)
            else:
                print(ser.errors)
        return cost_IT



# ec2_IT()