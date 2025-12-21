# Scenarios for accessing a DB instance in a VPC

Using Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources, such as Amazon RDS DB instances,
into a virtual private cloud (VPC). When you use Amazon VPC, you have control over your
virtual networking environment. You can choose your own IP address range, create
subnets, and configure routing and access control lists.

A VPC security group controls access to DB instances inside a VPC. Each VPC security group rule
enables a specific source to access a DB instance in a VPC that is associated with that VPC security group. The
source can be a range of addresses (for example, 203.0.113.0/24), or another VPC security group. By specifying a
VPC security group as the source, you allow incoming traffic from all instances (typically application servers)
that use the source VPC security group.

Before attempting to connect to your DB instance, configure your VPC for your use
case. The following are common scenarios for accessing a DB instance in a VPC:

- **A DB instance in a VPC accessed by an Amazon EC2 instance in the same VPC** –
  A common use of a DB instance in a VPC is to share data with an application server that is running in
  an EC2 instance in the same VPC. The EC2 instance might run a web server with an application that
  interacts with the DB instance.
- **A DB instance in a VPC accessed by an EC2 instance in a
  different VPC** – In some cases, your DB instance is in a
  different VPC from the EC2 instance that you're using to access it. If so,
  you can use VPC peering to access the DB instance.
- **A DB instance in a VPC accessed by a client application
  through the internet** – To access a DB instance in a VPC
  from a client application through the internet, you configure a VPC with a
  single public subnet. You also configure an internet gateway to enable
  communication over the internet.

To connect to a DB instance from outside of its VPC, the DB instance must be
publicly accessible. Also, access must be granted using the inbound rules of the
DB instance's security group, and other requirements must be met. For more
information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

- **A DB instance in a VPC accessed by a private network** –
  If your DB instance isn't publicly accessible, you can use one of the following options to
  access it from a private network:

      + An AWS Site-to-Site VPN connection
      + An Direct Connect connection
      + An AWS Client VPN connection

  For more information, see [Scenarios for accessing a DB instance in a VPC](USER_VPC.md "USER_VPC.md").
