For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Controlling access to a DB instance in a VPC

Using Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources, such as Amazon Timestream for InfluxDB DB instances,
into a virtual private cloud (VPC). When you use Amazon VPC, you have control over your virtual networking environment. You can choose your own IP address range, create subnets,
and configure routing and access control lists.

A VPC security group controls access to DB instances inside a VPC.
Each VPC security group rule enables a specific source to access a DB instance
in a VPC that is associated with that VPC security group.
The source can be a range of addresses (for example, 203.0.113.0/24), or another VPC security group. By specifying a VPC security group as the source, you allow incoming traffic from all instances (typically application servers) that use the source VPC security group.
Before attempting to connect to your DB instance, configure your VPC for
your use case. The following are common scenarios for accessing a DB instance in a VPC:

**A DB instance in a VPC accessed by an Amazon EC2 instance in the same VPC**
A common use of a DB instance in a VPC is to share data with an application server that is running in an EC2 instance in the same VPC. The EC2 instance might run a web server with an application that interacts with the DB instance.

**A DB instance in a VPC accessed by an EC2 instance in a different VPC**
In some cases, your DB instance is in a different VPC from the EC2 instance that you're using to access it.
If so, you can use VPC peering to access the DB instance.

**A DB instance in a VPC accessed by a client application
through the internet**
To access a DB instance in a VPC from a client application through the internet, you configure a VPC
with a single public subnet and use the public subnets to create the DB instance.
You also configure an internet gateway in the VPC to enable communication over the internet.
To connect to a DB instance from outside of its VPC, the DB instance must be publicly accessible.
Also, access must be granted using the inbound rules of the DB instance's
security group, and other requirements must be met.

For more information on VPC security groups, see [Control traffic to your AWS
resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md")
in the _Amazon Virtual Private Cloud User Guide_.

For details on how to connect to a Timestream for InfluxDB DB instance, see
[Connecting to an Amazon Timestream for InfluxDB DB instance](timestream-for-influx-db-connecting.md "timestream-for-influx-db-connecting.md").

## Security group scenario

A common use of a DB instance
in a VPC is to share data with an application
server running in an Amazon EC2 instance in the same VPC, which is accessed by a client
application outside the VPC. For this scenario, you use the Timestream for InfluxDB and VPC pages on the
AWS Management Console or the Timestream for InfluxDB and EC2 API operations to create the necessary instances and
security groups:

1. Create a VPC security group (for example, `sg-0123ec2example`) and define inbound rules
   that use the IP addresses of the client application as the source. This
   security group allows your client application to connect to EC2 instances in
   a VPC that uses this security group.
2. Create an EC2 instance for the application and add the EC2 instance to the VPC security group
   (`sg-0123ec2example`) that you created in the previous step.
3. Create a second VPC security group (for example, `sg-6789rdsexample`) and create a new rule
   by specifying the VPC security group that you created in step 1
   (`sg-0123ec2example`) as the source.
4. Create a new DB instance and add the DB instance to the VPC security group
   (`sg-6789rdsexample`) that you created in the previous step. When you
   create the DB, use the same port number as the one specified for the VPC security
   group (`sg-6789rdsexample`) rule that you created in step 3.

## Creating a VPC security group

You can create a VPC security group for a DB instance by using the
VPC console. For information about creating a security group, see [Create a security group
for your VPC](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md")
in the _Amazon Virtual Private Cloud User Guide_.

## Associating a security group with a DB instance

Once a Timestream for InfluxDB DB instance has been created, you will not be able to associate it to new
security groups since changes to these configurations are not currently supported.
