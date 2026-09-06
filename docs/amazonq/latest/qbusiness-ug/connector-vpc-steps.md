

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Configuring Amazon VPC support for Amazon Q Business connectors
<a name="connector-vpc-steps"></a>

To configure Amazon VPC for use with your Amazon Q Business connectors, take the following steps.

**Topics**
+ [Step 1. Create Amazon VPC subnets for Amazon Q Business](#connector-vpc-prerequisites-1)
+ [Step 2. Create Amazon VPC security groups for Amazon Q Business](#connector-vpc-prerequisites-2)
+ [Step 3. Configure your external data source and Amazon VPC](#connector-vpc-prerequisites-3)

## Step 1. Create Amazon VPC subnets for Amazon Q Business
<a name="connector-vpc-prerequisites-1"></a>

Create or choose an existing Amazon VPC subnet that Amazon Q Business can use to access your data source. The prepared subnets must be in one of the following AWS Regions and Availability Zones:
+ US West (Oregon)/us-west-2—usw2-az1, usw2-az2, usw2-az3
+ US East (N. Virginia)/us-east-1—use1-az1, use1-az2, use1-az4
+ Europe (Ireland)/eu-west-1—euw1-az1, euw1-az2, euw1-az3
+ Asia Pacific (Sydney)/ap-southeast-2—apse2-az1, apse2-az2, apse2-az3

Your data source must be accessible from the subnets that you provided to Amazon Q Business connector.

For more information about how to configure Amazon VPC subnets, see [Subnets for your Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

If Amazon Q Business must route the connection between two or more subnets, you can prepare multiple subnets. For example, the subnet that contains your data source is out of IP addresses. In that case, you can provide Amazon Q with an additional subnet that has sufficient IP addresses and connected to the first subnet. If you list multiple subnets, the subnets must be able to communicate with each other.

## Step 2. Create Amazon VPC security groups for Amazon Q Business
<a name="connector-vpc-prerequisites-2"></a>

To connect your Amazon Q Business data source connector to Amazon VPC, you must prepare one or more security groups from your VPC to assign to Amazon Q Business. The security groups will be associated to the elastic network interface created by Amazon Q Business. This network interface controls inbound and outbound traffic to and from Amazon Q Business when accessing the Amazon VPC subnets.

Make sure that your security group's outbound rules allow the traffic from Amazon Q Business data source connectors to access the subnets and the data source that you are going to sync with. For example, you might use an MySQL connector to sync from a MySQL database. If you're using the default port, the security groups must allow Amazon Q to access port 3306 on the host that runs the database.

We recommend that you configure a default security group with the following values for Amazon Q Business to use:
+ **Inbound rules** – If you choose to leave this empty, all inbound traffic will be blocked.
+ **Outbound rules** – Add one rule to allow all outbound traffic so that Amazon Q Business can initiate the requests to sync from your data source.
  + **IP version** – IPv4
  + **Type** – All traffic
  + **Protocol** – All traffic
  + **Port range** – All
  + **Destination** – 0.0.0.0/0

For more information about how to configure Amazon VPC security groups, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.

## Step 3. Configure your external data source and Amazon VPC
<a name="connector-vpc-prerequisites-3"></a>

Make sure that your external data source has the correct permissions configuration and network settings for Amazon Q Business to access it. You can find detailed instructions on how to configure your data sources in the prerequisites section of each connector page.

Also, check your Amazon VPC settings and make sure that your external data source is reachable from the subnet you will assign to Amazon Q Business. To do this, we recommend that you create an Amazon EC2 instance in the same subnet with the same security groups and test access to your data source from this Amazon EC2 instance. For more information, see [Troubleshooting Amazon VPC connection](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/vpc-connector-troubleshoot.html). 