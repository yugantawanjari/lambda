import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance = ec2.create_instances(
        ImageId='ami-071878317c449ae48',  # Replace with a valid AMI ID
        InstanceType='t2.micro',
        # 'KeyName': 'my-key-pair',  # Uncomment if using a key pair
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['sg-0f336e55dde122d70'],
        SubnetId='subnet-0ad818907a59a3f5b',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'MyEC2Instance'}
                ]
            }
        ],
        UserData='''#!/bin/bash
                       yum update -y
                       yum install -y httpd
                       systemctl start httpd
                       systemctl enable httpd'''
    )

    print('EC2 Instance created successfully.', instance[0].id)

# Example of triggering the lambda_handler function
if __name__ == "__main__":
    lambda_handler(None, None)
