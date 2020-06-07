import boto3
region = 'eu-west-2'
ec3=boto3.resource("ec2")
f={'Name':'instance-state-name','Values':['running']}
instances=[]
for each_in in ec3.instances.filter(Filters=[f]):
    #  print(each_in.private_ip_address)
       instances.append(each_in.id)
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
