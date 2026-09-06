

AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform).

# Tutorial: Using your own VPC and VPC peering
<a name="tutorial-using-own-network-vpc-peering"></a>

This tutorial presents a scenario that contains two VPCs, both with public and private subnets, a network address translation (NAT) gateway, and an internet gateway. 

This tutorial also contains an Amazon EC2 instance with a web server, security group, Refactor Spaces environment, application, service, and route. For more information about VPC peering, see [Work with VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html) in the *Amazon VPC Peering Guide*.

## Step 1: Set up a VPC in the environment owner account
<a name="tutorial-using-own-network-vpc-peering-setup-vpc-owner"></a>

**To set up the VPC in the environment owner account**

1. [Create a VPC](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html) with CIDR range 10.3.0.0/16 with one private subnet, one public subnet, and corresponding route tables.

1.  [Create and attach an internet gateway to your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway) and then add a [route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#subnet-route-tables) entry for the public subnet.

1.  [ Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the public subnet.

1. Create a route table entry for the [private subnet to route to the NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-nat). Use destination `0.0.0.0/0` and the target of the NAT gateway.

1. Create VPC peering in [different accounts and in the same AWS Region](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html#different-account-same-region). Share the VPC with the account that you want to share with the environment.

## Step 2: Set up a VPC for the service running in the service account
<a name="tutorial-using-own-network-vpc-peering-setup-vpc-service"></a>



**To set up the VPC for the service running in the service account**

1. Create a VPC with CIDR range 10.4.0.0/16 with one private subnet, one public subnet, and corresponding route tables.

1. Create and attach an internet gateway to your VPC and add a route table entry for the public subnet. 

1. Create a NAT gateway in the public subnet.

1. Create a route table entry for the private subnet to route to the NAT gateway. Use destination 0.0.0.0/0 and target of the NAT gateway.

1. [Accept VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/accept-vpc-peering-connection.html).

1. [Edit route table to route to VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html). For example, when you add a route, for **Destination**, enter 10.3.0.0/16 and for **Target**, enter pcx-0a02261b9c4f051f7-EXAMPLE.

## Step 3: Set up VPC peering in the environment owner account
<a name="tutorial-using-own-network-vpc-peering-setup-environ-owner"></a>



**To setup VPC peering in the environment owner account**
+ [Edit route table to route to VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html). For example, when you add a route, for **Destination**, enter 10.4.0.0/16 and for **Target**, enter pcx-0a02261b9c4f051f7-EXAMPLE.

## Step 4: Set up a web server in the service account
<a name="tutorial-using-own-network-vpc-peering-setup-web-server"></a>



**To setup a web server in the service account**

1. [Create an Amazon EC2 instance in the private subnet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html).

1. [Install a web server on the Amazon EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html). Run the web server on any port, for example, port 3000.

1.  [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#creating-security-groups) in the VPC with an inbound rule that allows traffic from the environment owner account CIDR range to the server port, for example, 10.4.0.0/16 to port 3000.

1. [Add the security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#assigning-security-group) to the Amazon EC2 instance.

## Step 5: Set up a Refactor Spaces environment and application in the environment owner account
<a name="tutorial-using-own-network-vpc-peering-setup-environ-app-owner"></a>

Before you begin this step, make sure that you are using the [AWS managed policy: AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess) managed policy and the [Extra required permissions policy for environments without a network bridge](security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions) policy.

**To set up an environment and an application in the environment owner account**

1. In the environment account, create a Refactor Spaces environment with network fabric type NONE. Make sure to share the environment with the service account that serves as the environment account.

1. In the environment account, create an application with proxy VPC of the 10.3.0.0/16 CIDR range in environment owner account.

## Step 6: Set up Refactor Spaces in the service account
<a name="tutorial-using-own-network-vpc-peering-setup-eervice"></a>



**To set up Refactor Spaces in the service account**

1. In the service account, create a service pointing to the URL of your EC2 instance.

1. In the service account, create a default route to the EC2 instance. 

1. To test that the route works, visit the Refactor Spaces API Gateway URL, as shown in the following example.

   ```
   curl https://x8awx61hm3-EXAMPLE.execute-api.us-west-2.amazonaws.com/prod
   ```