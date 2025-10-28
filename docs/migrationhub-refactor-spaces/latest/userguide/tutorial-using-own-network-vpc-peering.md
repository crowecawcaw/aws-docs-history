AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Tutorial: Using your own VPC

and VPC peering

This tutorial presents a scenario that contains
two VPCs, both with public and private subnets, a network address translation (NAT)
gateway, and an internet gateway.

This tutorial also contains an Amazon EC2 instance with a web server, security group,
Refactor Spaces environment, application, service, and route. For more information about VPC
peering, see [Work with VPC peering
connections](../../../vpc/latest/peering/working-with-vpc-peering.md "../../../vpc/latest/peering/working-with-vpc-peering.md") in the _Amazon VPC Peering Guide_.

## Step 1: Set

up a VPC in the environment owner account

###### To set up the VPC in the environment owner account

1. [Create a
   VPC](../../../directoryservice/latest/admin-guide/gsg_create_vpc.md "../../../directoryservice/latest/admin-guide/gsg_create_vpc.md") with CIDR range 10.3.0.0/16 with one private subnet, one
   public subnet, and corresponding route tables.
2. [Create and attach an internet gateway to your VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway") and then add
   a [route table](../../../vpc/latest/userguide/VPC_Route_Tables.md#subnet-route-tables "../../../vpc/latest/userguide/VPC_Route_Tables.md#subnet-route-tables") entry for the public subnet.
3. [Create a NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") in the public subnet.
4. Create a route table entry for the [private subnet to route to the NAT gateway](../../../vpc/latest/userguide/route-table-options.md#route-tables-nat "../../../vpc/latest/userguide/route-table-options.md#route-tables-nat"). Use destination
   `0.0.0.0/0` and the target of the NAT gateway.
5. Create VPC peering in [different accounts and in the same AWS Region](../../../vpc/latest/peering/create-vpc-peering-connection.md#different-account-same-region "../../../vpc/latest/peering/create-vpc-peering-connection.md#different-account-same-region"). Share the VPC
   with the account that you want to share with the environment.

## Step 2:

Set up a VPC for the service running in the service account

###### To set up the VPC for the service running in the service account

1. Create a VPC with CIDR range 10.4.0.0/16 with one private subnet, one
   public subnet, and corresponding route tables.
2. Create and attach an internet gateway to your VPC and add a route table
   entry for the public subnet.
3. Create a NAT gateway in the public subnet.
4. Create a route table entry for the private subnet to route to the NAT
   gateway. Use destination 0.0.0.0/0 and target of the NAT gateway.
5. [Accept VPC
   peering connection](../../../vpc/latest/peering/accept-vpc-peering-connection.md "../../../vpc/latest/peering/accept-vpc-peering-connection.md").
6. [Edit route table to
   route to VPC peering](../../../vpc/latest/peering/vpc-peering-routing.md "../../../vpc/latest/peering/vpc-peering-routing.md"). For example, when you add a route, for
   **Destination**, enter 10.3.0.0/16 and for
   **Target**, enter pcx-0a02261b9c4f051f7-EXAMPLE.

## Step 3:

Set up VPC peering in the environment owner account

###### To setup VPC peering in the environment owner account

- [Edit route table to
  route to VPC peering](../../../vpc/latest/peering/vpc-peering-routing.md "../../../vpc/latest/peering/vpc-peering-routing.md"). For example, when you add a route, for
  **Destination**, enter 10.4.0.0/16 and for
  **Target**, enter pcx-0a02261b9c4f051f7-EXAMPLE.

## Step 4:

Set up a web server in the service account

###### To setup a web server in the service account

1. [Create an
   Amazon EC2 instance in the private subnet](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md").
2. [Install a web server on the Amazon EC2 instance](../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md "../../../AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.md"). Run the web server
   on any port, for example, port 3000.
3. [Create a security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md#creating-security-groups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#creating-security-groups") in the VPC with an inbound rule that
   allows traffic from the environment owner account CIDR range to the server
   port, for example, 10.4.0.0/16 to port 3000.
4. [Add the security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#assigning-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#assigning-security-group") to the Amazon EC2 instance.

##

Step 5: Set up a Refactor Spaces environment and application in the environment owner
account

Before you begin this step, make sure that you are using the [AWS managed policy:
AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess") managed policy and the [Extra required permissions policy for environments without a network
bridge](security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions "security-iam-awsmanpol.md#security-iam-awsmanpol-policies-no-network-bridge-extra-permissions") policy.

###### To set up an environment and an application in the environment owner

account

1. In the environment account, create a Refactor Spaces environment with network
   fabric type NONE. Make sure to share the environment with the service
   account that serves as the environment account.
2. In the environment account, create an application with proxy VPC of the
   10.3.0.0/16 CIDR range in environment owner account.

## Step 6: Set

up Refactor Spaces in the service account

###### To set up Refactor Spaces in the service account

1. In the service account, create a service pointing to the URL of your EC2
   instance.
2. In the service account, create a default route to the EC2 instance.
3. To test that the route works, visit the Refactor Spaces API Gateway URL, as
   shown in the following example.

```
curl https://x8awx61hm3-EXAMPLE.execute-api.us-west-2.amazonaws.com/prod
```
