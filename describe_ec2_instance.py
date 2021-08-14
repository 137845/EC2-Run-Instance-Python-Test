import boto3

def describe_ec2_instance():
    try:
        print("Describe EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instance()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

describe_ec2_instance()
    
