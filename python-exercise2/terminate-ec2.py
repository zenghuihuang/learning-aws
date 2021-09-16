import boto3
import pprint

ec2_client = boto3.client("ec2", region_name="us-east-2")
reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(reservations)

for reservation in reservations:
    for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            ec2_client.terminate_instances(InstanceIds=[instance_id])
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
           # print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")


    
     
    
