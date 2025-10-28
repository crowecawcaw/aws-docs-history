# Elastic Disaster Recovery network setting

preparations

###### Topics

- [Staging area subnet](#Staging-Area "#Staging-Area")
- [Network requirements](#Setting-Up-Network "#Setting-Up-Network")
- [Operational subnets](#Operational-Subnet "#Operational-Subnet")

## Staging area subnet

Before setting up AWS Elastic Disaster Recovery (AWS DRS), you should create a subnet which will
be used by AWS DRS as a staging area for data replicated from your
source servers to AWS. You must specify this subnet in the replication template. You
can override this subnet for specific source servers in the replication settings.
While you can use an existing subnet in your AWS account, the best practice is to
create a new dedicated subnet for this purpose. Learn more about
[replication settings](replication-settings.md "replication-settings.md").

###### Note

When planning to recover into an AWS Local Zone, we recommend setting the staging area subnet within
the AWS Region, and not the AWS Local Zone. This ensures optimal launch conditions for the replication
servers and conversion servers involved in the recovery process. However, if your recovery requirements
necessitate the use of the AWS Local Zone for the staging area subnet, we recommend performing recovery
drills to validate that you can replicate and recover your production workloads without any issues.

## Network requirements

The replication servers launched by AWS Elastic Disaster Recovery in your staging area subnet
need to be able to send data over TCP port 443 to the AWS Elastic Disaster Recovery API endpoint at
https://drs.{region}.amazonaws.com/. Replace “{region}” with the AWS Region code you are
replicating to, for example “us-east-1” .

The source servers on which the AWS Replication Agent is installed need be able to send
data over TCP port 1500 to the Replication Servers in the staging area subnet. They also need to
be able to send data to AWS DRS's API endpoint at
https://drs.{region}.amazonaws.com/. Replace “{region}” with the AWS Region code you are
replicating to, for example “us-east-1” .

## Operational subnets

Drill and recovery instances are launched in a subnet you specify in the Amazon EC2 launch template
associated with each source server. The Amazon EC2 launch template is created automatically when you add a source server to AWS Elastic Disaster Recovery.
