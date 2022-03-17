import boto3

client = boto3.client('cloudtrail')
#s3 = boto3.resource('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)
for trail in client.list_trails():
    print(trail)