#first, I had to do this in the console $ python3 -m pip install boto3
#also make sure amazon CLI is set up.
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

print("*****Printing all of the s3 Bucket Names\n")
for bucket in s3.buckets.all():
    print(bucket.name)

#ec2 stuff
print("*****Printing describe instances of EC2 Instances\n")
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response, '\n')

print("*****Printing describe Regions\n")
response = ec2.describe_regions()
print('Regions:', response['Regions'], '\n')


#tags

client = boto3.client('resourcegroupstaggingapi')
print("*****Printing the Tag Keys\n")
response = client.get_tag_keys()
print('Tag Keys:', response['TagKeys'],'\n')

print("*****Printing the Values of each Tag Key\n")
for key in response['TagKeys']:
    print("Tag Key:", key,)
    valueResponse = client.get_tag_values(
        PaginationToken='',
        Key=key
    )
    print('Tag Values:', valueResponse['TagValues'], '\n'
    )