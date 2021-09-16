import argparse,sys
import boto3




#This function will be executed when the file is run from command line and not imported. 
def main():
    create_ec2_instances()
   

#This function creates one instance with the name specified by the user.
#The name of the instance is passed as an argument from command line.
def create_ec2_instances():
    ec2 = boto3.resource('ec2')
    #input_name = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Insert the name of the instance that you want to create: ")
    args = parser.parse_args()
    print(args.name)
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
                    'Value': args.name
                },
            ]
        },
    ] 
    )

if __name__ == "__main__":
    main()









 
