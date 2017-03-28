from __future__ import print_function
import json
import boto3

print('Loading function')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Intel_Edison')
data_list = []


def lambda_Dynamo(event, context):
    print("Received event: " + str(event))
    value1 = str(event['TimeStamp'])
    value2 = str(event['light'])
    value3 = str(event['temperature'])
    value4 = str(event['moisture'])
    value5 = str(event['humidity'])
    print("value1 = " + value1)
    print("value2 = " + value2)
    print("value3 = " + value3)
    print("value4 = " + value4)
    print("value4 = " + value5)
    data_list.append({
        'TimeStamp': value1,
        'light': value2,
        'temperature': value3,
        'moisture': value4,
        'humidity': value5,
    })
    if len(data_list) > 199:
        table.delete_item(
            Key={
                'TimeStamp': data_list[0]['TimeStamp']
            }
        )

    table.put_item(
        Item={
            'TimeStamp': value1,
            'light': value2,
            'temperature': value3,
            'moisture': value4,
            'humidity': value5,
        }
    )
