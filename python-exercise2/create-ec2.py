import sys
import boto3
ec2 = boto3.resource('ec2')
input_name = sys.argv[1]

instance = ec2.create_instances(
    ImageId='ami-00dfe2c7ce89a450b',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': input_name
                },
            ]
        },
    ] 


)




 
