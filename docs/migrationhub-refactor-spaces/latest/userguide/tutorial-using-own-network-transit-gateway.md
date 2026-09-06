

AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform).

# Tutorial: Using your own AWS Transit Gateway
<a name="tutorial-using-own-network-transit-gateway"></a>

The following tutorial presents an example of how to use your own AWS Transit Gateway with Refactor Spaces.

In this tutorial, the VPC setup contains two VPCs, both with public and private subnets, a network address translation (NAT) gateway and an internet gateway. The tutorial also contains an Amazon EC2 instance with a web server, security groups, a Refactor Spaces environment, application, service, and route. Traffic flows to the private URL endpoint of a web server through your transit gateway. For more information, see [VPC with public and private subnets (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html).

## Step 1: Set up a VPC in the environment owner account
<a name="tutorial-using-own-network-gateway-setup-vpc-owner"></a>

**To set up a VPC in the environment owner account**

1. [Create a VPC](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html) with CIDR range 10.1.0.0/16 with one private subnet and one public subnet, and corresponding route tables.

1. [Create and attach an internet gateway to your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway), and add a [route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#subnet-route-tables) entry for the public subnet.

1. [ Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the public subnet.

1. Create a route table entry for the [private subnet to route to the NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-nat). Use destination 0.0.0.0/0 and the target of the NAT gateway. 

## Step 2: Set up a VPC in the service account
<a name="tutorial-using-own-network-gateway-setup-vpc-service"></a>



**To set up a VPC in the service account**

1. Create a VPC with a CIDR range of 10.2.0.0/16 with one private subnet and one public subnet, and corresponding route tables.

1. Create and attach an internet gateway to your VPC, and add a route table entry for the public subnet.

1. Create a NAT gateway in the public subnet.

1. Create a route table entry for the private subnet to route to the NAT gateway. Use destination 0.0.0.0/0 and the target of the NAT gateway.

## Step 3: Set up a web server in the service account VPC.
<a name="tutorial-using-own-network-gateway-setup-web-server"></a>



**To set up the web server in the service account VPC**

1. [Create an Amazon EC2 instance in the private subnet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html).

1. [Install a web server on the Amazon EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html).

1. [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#creating-security-groups) in a member VPC with an inbound rule allowing traffic from the CIDR in Environment Owner Account 10.1.0.0/16.

1. [Add the security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#assigning-security-group) to the Amazon EC2 instance.

## Step 4: Set up Transit Gateway in the environment owner account
<a name="tutorial-using-own-network-gateway-setup-owner"></a>



**To set up Transit Gateway in the environment owner account**

1. [Create a Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#create-tgw) in this account with all the defaults. For more information, see [Getting started with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html) in the *Amazon VPC Transit Gateways user guide*.

1. Create a VPC attachment to the VPC with all the defaults.

1. [Add a route](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes) in the main route table of the VPC. Direct the route to the CIDR range of the other VPC.

1. [Associate the subnet route table of the VPC](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AssociateSubnet) with the [main route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#main-route-table).

## Step 5: Set up Transit Gateway in the service account
<a name="tutorial-using-own-network-gateway-setup-owner"></a>



**To set up Transit Gateway in the service account**

1. Share Transit Gateway with service account with the AWS RAM console from environment account.

1. Accept the resource share from service account.

1. Create a Transit Gateway attachment from the service account to the VPC with all the defaults and the two private subnets.

1. Accept the Transit Gateway attachment from environment account.

1. Add a route in the main route table of the VPC. Direct the route to the CIDR range of the other VPC.

1. [Associate the subnet route table of the VPC](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AssociateSubnet) with the [main route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#main-route-table). 

Now you should have two VPCs with Transit Gateway routing set up.

## Step 6: Set up a Refactor Spaces environment and application in the environment owner account
<a name="tutorial-using-own-network-gateway-setup-environ-app-owner"></a>

 

Before you begin this step, make sure that you are using the [AWS managed policy: AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess) managed policy and the [Extra required permissions policy for environments without a network bridge](security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions) policy.

**To set up a Refactor Spaces environment and application in the environment owner account**

1. In the environment owner account, create a Refactor Spaces environment with network fabric type NONE. Make sure to share the environment with the service account.

1. In the environment owner account, create an application with proxy VPC of the 10.1.0.0/16 CIDR range in **Environment owner account**.

## Step 7: Set up a Refactor Spaces service in the service account
<a name="tutorial-using-own-network-gateway-setup-service"></a>



**To set up a Refactor Spaces service in the service account**

1. In the service account, create a service that points to the URL of Amazon EC2 instance.

1. In the service development account, create a default route to the EC2 instance.

1. To test that the route works, visit the Refactor Spaces API Gateway URL, as shown in the following example.

   ```
   curl https://x8awx61hm3-EXAMPLE.execute-api.us-west-2.amazonaws.com/prod
   ```