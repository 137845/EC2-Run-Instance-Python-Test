import boto3
s3 = boto3.resource('s3')
obj = s3.Object('qi-s3-bucket-test101', 'newtest.txt')
body = obj.get()['Body'].read()
