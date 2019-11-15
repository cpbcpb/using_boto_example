#first, I had to do this in the console $ python3 -m pip install boto3
#also make sure amazon CLI is set up.
import boto3

#ec2 stuff
print("*****Printing describe instances of EC2 Instances\n")
ec2 = boto3.client('ec2')

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance, '\n')
# write an output file with entire response.  This will overwrite anything previous.
f=open("./Results/ec2_descriptions.json", "w+")
f.write("{'Results of ec2.describe_instances in boto3': %s}" % (response))
f.close()
print("File ec2_descriptions.json was created or updated in the Results folder.")

print("Open ec2_descriptions.json in Results folder to see")