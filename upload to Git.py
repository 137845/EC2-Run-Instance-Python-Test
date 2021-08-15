import boto3

def describe_ec2_instance():
    try:
        print("Describe EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instance()["Reservation"][0]["Instance"][0]["InstanceId"])
        return str(resource_ec2.describe_instance()["Reservation"][0]["Instance"][0]["InstanceId"])
    except Exception as e:
        print(e)


def reboot_ec2_instance():
    try:
        print("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        resource_ec2.reboot_instances(InstanceIds = [instance_id])

    except Exception as e:
        print(e)

reboot_ec2_instance()
    
