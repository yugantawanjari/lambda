import boto3

# ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
def lambda_handler(event, context):
    response = client.start_instances(
    InstanceIds=[
        'i-01f133ef60da40290',
    ],
    )
