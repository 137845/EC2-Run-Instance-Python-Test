import boto3

def create_ec2_instance():

    try:
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(

            ImageId = "ami-0c2b8ca1dad447f8a",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t2.micro",
            KeyName = "devops101"

        )
    
    except Exception as e:
        print(e)


create_ec2_instance()

    
