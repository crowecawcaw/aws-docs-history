AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Tutorial: Using your own

AWS Transit Gateway

The following tutorial presents an example of how to use your own AWS Transit Gateway with
Refactor Spaces.

In this tutorial, the VPC setup contains two VPCs, both with public and private
subnets, a network address translation (NAT) gateway and an internet gateway. The
tutorial also contains an Amazon EC2 instance with a web server, security groups, a Refactor Spaces
environment, application, service, and route. Traffic flows to the private URL endpoint
of a web server through your transit gateway. For more information, see [VPC with public
and private subnets (NAT)](../../../vpc/latest/userguide/VPC_Scenario2.md "../../../vpc/latest/userguide/VPC_Scenario2.md").

## Step 1: Set up

a VPC in the environment owner account

###### To set up a VPC in the environment owner account

1. [Create a
   VPC](../../../directoryservice/latest/admin-guide/gsg_create_vpc.md "../../../directoryservice/latest/admin-guide/gsg_create_vpc.md") with CIDR range 10.1.0.0/16 with one private subnet and one
   public subnet, and corresponding route tables.
2. [Create and attach an internet gateway to your VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway"), and add a
   [route table](../../../vpc/latest/userguide/VPC_Route_Tables.md#subnet-route-tables "../../../vpc/latest/userguide/VPC_Route_Tables.md#subnet-route-tables") entry for the public subnet.
3. [Create a NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") in the public subnet.
4. Create a route table entry for the [private subnet to route to the NAT gateway](../../../vpc/latest/userguide/route-table-options.md#route-tables-nat "../../../vpc/latest/userguide/route-table-options.md#route-tables-nat"). Use destination
   0.0.0.0/0 and the target of the NAT gateway.

## Step 2: Set

up a VPC in the service account

###### To set up a VPC in the service account

1. Create a VPC with a CIDR range of 10.2.0.0/16 with one private subnet and
   one public subnet, and corresponding route tables.
2. Create and attach an internet gateway to your VPC, and add a route table
   entry for the public subnet.
3. Create a NAT gateway in the public subnet.
4. Create a route table entry for the private subnet to route to the NAT
   gateway. Use destination 0.0.0.0/0 and the target of the NAT gateway.

## Step 3: Set up

a web server in the service account VPC.

###### To set up the web server in the service account VPC

1. [Create an
   Amazon EC2 instance in the private subnet](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md").
2. [Install a web server on the Amazon EC2 instance](../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md "../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md").
3. [Create a security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md#creating-security-groups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#creating-security-groups") in a member VPC with an inbound rule
   allowing traffic from the CIDR in Environment Owner Account
   10.1.0.0/16.
4. [Add the security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#assigning-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#assigning-security-group") to the Amazon EC2 instance.

## Step 4: Set up

Transit Gateway in the environment owner account

###### To set up Transit Gateway in the environment owner account

1. [Create a
   Transit Gateway](../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw "../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw") in this account with all the defaults. For more
   information, see [Getting started with
   transit gateways](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md") in the _Amazon VPC Transit Gateways user
   guide_.
2. Create a VPC attachment to the VPC with all the defaults.
3. [Add
   a route](../../../vpc/latest/userguide/WorkWithRouteTables.md#AddRemoveRoutes "../../../vpc/latest/userguide/WorkWithRouteTables.md#AddRemoveRoutes") in the main route table of the VPC. Direct the route to
   the CIDR range of the other VPC.
4. [Associate the subnet route table of the VPC](../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet "../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet") with the [main
   route table](../../../vpc/latest/userguide/VPC_Route_Tables.md#main-route-table "../../../vpc/latest/userguide/VPC_Route_Tables.md#main-route-table").

## Step 5: Set up

Transit Gateway in the service account

###### To set up Transit Gateway in the service account

1. Share Transit Gateway with service account with the AWS RAM console from environment
   account.
2. Accept the resource share from service account.
3. Create a Transit Gateway attachment from the service account to the VPC with all
   the defaults and the two private subnets.
4. Accept the Transit Gateway attachment from environment account.
5. Add a route in the main route table of the VPC. Direct the route to the
   CIDR range of the other VPC.
6. [Associate the subnet route table of the VPC](../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet "../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet") with the [main
   route table](../../../vpc/latest/userguide/VPC_Route_Tables.md#main-route-table "../../../vpc/latest/userguide/VPC_Route_Tables.md#main-route-table").

Now you should have two VPCs with Transit Gateway routing set up.

## Step 6:

Set up a Refactor Spaces environment and application in the environment owner account

Before you begin this step, make sure that you are using the [AWS managed policy:
AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess") managed policy and the [Extra required permissions policy for environments without a network
bridge](security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions "security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions") policy.

###### To set up a Refactor Spaces environment and application in the environment owner

account

1. In the environment owner account, create a Refactor Spaces environment with
   network fabric type NONE. Make sure to share the environment with the
   service account.
2. In the environment owner account, create an application with proxy VPC of
   the 10.1.0.0/16 CIDR range in **Environment owner
   account**.

## Step 7: Set up a

Refactor Spaces service in the service account

###### To set up a Refactor Spaces service in the service account

1. In the service account, create a service that points to the URL of Amazon EC2
   instance.
2. In the service development account, create a default route to the EC2
   instance.
3. To test that the route works, visit the Refactor Spaces API Gateway URL, as
   shown in the following example.

```
curl https://x8awx61hm3-EXAMPLE.execute-api.us-west-2.amazonaws.com/prod
```
