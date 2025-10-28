# Managing your own Amazon VPC endpoints on Amazon MWAA

Amazon MWAA uses Amazon VPC endpoints to integrate with various AWS services necessary to set up an Apache Airflow environment. Managing your own endpoints has two primary use cases:

1. It means you can create Apache Airflow environments in a shared Amazon VPC when you use an
   [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") to manage
   multiple AWS accounts and share resources.
2. It lets you use more restrictive access policies by narrowing down your permissions to the specific resources that use your endpoints.
   If you choose to manage your own VPC endpoints, you're responsible for creating your own endpoints for the environment RDS for PostgreSQL database and for the environment webserver.

For more information about how Amazon MWAA deploys Apache Airflow in the cloud, refer to the [Amazon MWAA architecture diagram](what-is-mwaa.md#architecture-mwaa "what-is-mwaa.md#architecture-mwaa").

###### Important

Amazon MWAA does not validate the IP address type (`AddressType`) selection for customer-managed endpoints, so make sure you correctly specify `AddressType` (valid options are IPv4 or IPv6).

## Creating an environment in a shared Amazon VPC

If you use [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") to
manage multiple AWS accounts that share resources, you can use customer-managed VPC
endpoints with Amazon MWAA to share environment resources with another account in your
organization.

When you configure shared VPC access, the account that owns the main Amazon VPC (_owner_) shares the two private subnets
required by Amazon MWAA with other accounts (_participants_) that belong to the same organization. Participant accounts that share those subnets
can view, create, modify, and delete environments in the shared Amazon VPC.

Assume you have an account, `Owner`, which acts as the `Root` account in the organization and owns the Amazon VPC resources,
and a participant account, `Participant`, a member of the same organization. When `Participant` creates
a new Amazon MWAA in Amazon VPC it shares with `Owner`, Amazon MWAA will first create the service VPC resources,
then enter a [`PENDING`](../API/API_Environment.md#mwaa-Type-Environment-Status "../API/API_Environment.md#mwaa-Type-Environment-Status") state for up to 72 hours.

After the environment status changes from `CREATING` to `PENDING`, a principal acting on behalf of `Owner` creates the required endpoints.
To do this, Amazon MWAA lists the database and webserver endpoint in the Amazon MWAA console. You can also call the `GetEnvironment` API action to get the service endpoints.

###### Note

If the Amazon VPC you use to share resources is a private Amazon VPC, you must still complete the steps described in [Managing access to service-specific Amazon VPC endpoints on Amazon MWAA](vpc-vpe-access.md "vpc-vpe-access.md"). The topic covers setting up a different set of Amazon VPC
endpoints related to other AWS services that AWS integrates with, such as Amazon ECR, Amazon ECS, and Amazon SQS. These services are essential in operating, and managing, your Apache Airflow environment
in the cloud.

### Prerequisites

Before you create an Amazon MWAA environment in a shared VPC, you need the following resources:

- An AWS account, `Owner` to be used as the account that owns the Amazon VPC.
- An [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
  organization unit, `MyOrganization` created as a
  _root_.
- A second AWS account, `Participant`, under `MyOrganization` to serve the participant account that creates the
  new environment.

In addition, we recommend that you familiarize yourself with the [responsibilities and permissions for owners and participants](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations")
when sharing resources in Amazon VPC.

### Create the Amazon VPC

First, create a new Amazon VPC that the owner and participant accounts will share:

1. Sign in to the console using `Owner`, then, open the AWS CloudFormation console. Use the following template to create a stack. This stack
   provisions a number of networking resources including a Amazon VPC, and the subnets that the two accounts will share in this scenario.

```
AWSTemplateFormatVersion: "2010-09-09"
Description: >-
This template deploys a VPC, with a pair of public and private subnets spread across two Availability Zones. It deploys an internet gateway, with a default route on the public subnets. It deploys a pair of NAT gateways (one in each AZ), and default routes for them in the private subnets.
 Parameters:
   EnvironmentName:
     Description: An environment name that is prefixed to resource names
     Type: String
     Default: mwaa-
   VpcCIDR:
     Description: Please enter the IP range (CIDR notation) for this VPC
     Type: String
     Default: 10.192.0.0/16
   PublicSubnet1CIDR:
     Description: >-
     Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone
     Type: String
     Default: 10.192.10.0/24
   PublicSubnet2CIDR:
     Description: >-
     Please enter the IP range (CIDR notation) for the public subnet in the	second Availability Zone
     Type: String
     Default: 10.192.11.0/24
   PrivateSubnet1CIDR:
     Description: >-
     Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone
     Type: String
     Default: 10.192.20.0/24
   PrivateSubnet2CIDR:
     Description: >-
     Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone
     Type: String
     Default: 10.192.21.0/24
 Resources:
   VPC:
     Type: 'AWS::EC2::VPC'
     Properties:
     CidrBlock: !Ref VpcCIDR
     EnableDnsSupport: true
     EnableDnsHostnames: true
     Tags:
       - Key: Name
       Value: !Ref EnvironmentName
   InternetGateway:
     Type: 'AWS::EC2::InternetGateway'
     Properties:
     Tags:
       - Key: Name
       Value: !Ref EnvironmentName
   InternetGatewayAttachment:
     Type: 'AWS::EC2::VPCGatewayAttachment'
     Properties:
       InternetGatewayId: !Ref InternetGateway
       VpcId: !Ref VPC
   PublicSubnet1:
     Type: 'AWS::EC2::Subnet'
     Properties:
       VpcId: !Ref VPC
       AvailabilityZone: !Select
         - 0
         - !GetAZs ''
       CidrBlock: !Ref PublicSubnet1CIDR
       MapPublicIpOnLaunch: true
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Public Subnet (AZ1)'
   PublicSubnet2:
     Type: 'AWS::EC2::Subnet'
     Properties:
						VpcId: !Ref VPC
       AvailabilityZone: !Select
         - 1
         - !GetAZs ''
       CidrBlock: !Ref PublicSubnet2CIDR
       MapPublicIpOnLaunch: true
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Public Subnet (AZ2)'
   PrivateSubnet1:
     Type: 'AWS::EC2::Subnet'
     Properties:
       VpcId: !Ref VPC
       AvailabilityZone: !Select
         - 0
         - !GetAZs ''
       CidrBlock: !Ref PrivateSubnet1CIDR
       MapPublicIpOnLaunch: false
         Tags:
         - Key: Name
           Value: !Sub '${EnvironmentName} Private Subnet (AZ1)'
   PrivateSubnet2:
     Type: 'AWS::EC2::Subnet'
     Properties:
       VpcId: !Ref VPC
       AvailabilityZone: !Select
         - 1
         - !GetAZs ''
       CidrBlock: !Ref PrivateSubnet2CIDR
       MapPublicIpOnLaunch: false
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Private Subnet (AZ2)'
   NatGateway1EIP:
     Type: 'AWS::EC2::EIP'
     DependsOn: InternetGatewayAttachment
     Properties:
       Domain: vpc
   NatGateway2EIP:
     Type: 'AWS::EC2::EIP'
     DependsOn: InternetGatewayAttachment
     Properties:
       Domain: vpc
   NatGateway1:
     Type: 'AWS::EC2::NatGateway'
     Properties:
       AllocationId: !GetAtt NatGateway1EIP.AllocationId
       SubnetId: !Ref PublicSubnet1
   NatGateway2:
     Type: 'AWS::EC2::NatGateway'
     Properties:
       AllocationId: !GetAtt NatGateway2EIP.AllocationId
       SubnetId: !Ref PublicSubnet2
   PublicRouteTable:
     Type: 'AWS::EC2::RouteTable'
     Properties:
       VpcId: !Ref VPC
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Public Routes'
   DefaultPublicRoute:
     Type: 'AWS::EC2::Route'
     DependsOn: InternetGatewayAttachment
     Properties:
       RouteTableId: !Ref PublicRouteTable
       DestinationCidrBlock: 0.0.0.0/0
       GatewayId: !Ref InternetGateway
   PublicSubnet1RouteTableAssociation:
     Type: 'AWS::EC2::SubnetRouteTableAssociation'
     Properties:
       RouteTableId: !Ref PublicRouteTable
       SubnetId: !Ref PublicSubnet1
   PublicSubnet2RouteTableAssociation:
     Type: 'AWS::EC2::SubnetRouteTableAssociation'
     Properties:
       RouteTableId: !Ref PublicRouteTable
       SubnetId: !Ref PublicSubnet2
   PrivateRouteTable1:
     Type: 'AWS::EC2::RouteTable'
     Properties:
       VpcId: !Ref VPC
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Private Routes (AZ1)'
   DefaultPrivateRoute1:
     Type: 'AWS::EC2::Route'
     Properties:
       RouteTableId: !Ref PrivateRouteTable1
       DestinationCidrBlock: 0.0.0.0/0
       NatGatewayId: !Ref NatGateway1
   PrivateSubnet1RouteTableAssociation:
     Type: 'AWS::EC2::SubnetRouteTableAssociation'
     Properties:
       RouteTableId: !Ref PrivateRouteTable1
       SubnetId: !Ref PrivateSubnet1
   PrivateRouteTable2:
     Type: 'AWS::EC2::RouteTable'
     Properties:
       VpcId: !Ref VPC
       Tags:
         - Key: Name
         Value: !Sub '${EnvironmentName} Private Routes (AZ2)'
   DefaultPrivateRoute2:
     Type: 'AWS::EC2::Route'
     Properties:
       RouteTableId: !Ref PrivateRouteTable2
       DestinationCidrBlock: 0.0.0.0/0
       NatGatewayId: !Ref NatGateway2
   PrivateSubnet2RouteTableAssociation:
     Type: 'AWS::EC2::SubnetRouteTableAssociation'
     Properties:
       RouteTableId: !Ref PrivateRouteTable2
       SubnetId: !Ref PrivateSubnet2
   SecurityGroup:
     Type: 'AWS::EC2::SecurityGroup'
     Properties:
       GroupName: mwaa-security-group
       GroupDescription: Security group with a self-referencing inbound rule.
       VpcId: !Ref VPC
   SecurityGroupIngress:
     Type: 'AWS::EC2::SecurityGroupIngress'
     Properties:
       GroupId: !Ref SecurityGroup
       IpProtocol: '-1'
       SourceSecurityGroupId: !Ref SecurityGroup
       Outputs:
         VPC:
           Description: A reference to the created VPC
           Value: !Ref VPC
           PublicSubnets:
           Description: A list of the public subnets
           Value: !Join
             - ','
             - - !Ref PublicSubnet1
             - !Ref PublicSubnet2
         PrivateSubnets:
           Description: A list of the private subnets
           Value: !Join
             - ','
             - - !Ref PrivateSubnet1
             - !Ref PrivateSubnet2
         PublicSubnet1:
           Description: A reference to the public subnet in the 1st Availability Zone
           Value: !Ref PublicSubnet1
         PublicSubnet2:
           Description: A reference to the public subnet in the 2nd Availability Zone
           Value: !Ref PublicSubnet2
         PrivateSubnet1:
           Description: A reference to the private subnet in the 1st Availability Zone
           Value: !Ref PrivateSubnet1
         PrivateSubnet2:
           Description: A reference to the private subnet in the 2nd Availability Zone
           Value: !Ref PrivateSubnet2
         SecurityGroupIngress:
           Description: Security group with self-referencing inbound rule
           Value: !Ref SecurityGroupIngress
```

2. After the new Amazon VPC resources have been provisioned, navigate to the AWS Resource Access Manager console, then choose **Create resource share**.
3. Choose the subnets you created in the first step from the list of available subnets you can share with `Participant`.

### Create the environment

Complete the following steps to create an Amazon MWAA environment with customer-managed Amazon VPC endpoints.

1. Sign in using `Participant`, and open the Amazon MWAA console. Complete **Step one: Specify details** to specify an Amazon S3 bucket, a DAG folder,
   and dependencies for your new environment. For more information, refer to [getting started](create-environment.md#create-environment-start-details "create-environment.md#create-environment-start-details").
2. On the **Configure advanced settings** page, under **Networking**, choose the subnets from the shared Amazon VPC.
3. Under **Endpoint management** choose **CUSTOMER** from the dropdown list.
4. Keep the default for the remaining options on the page, then, choose **Create environment** on the **Review and create** page.

The environment begins in a `CREATING` state, then changes to `PENDING`. When the environment is `PENDING`,
write down the **Database endpoint service name** and **webserver endpoint service name** (if you set up a private webserver)
using the console.

When you create a new environment using the Amazon MWAA console. Amazon MWAA creates a new security group with the required inbound and outbound rules. Write down the
security group ID.

In the next section, `Owner` will use the service endpoints and the security group ID to create new Amazon VPC endpoints in the shared Amazon VPC.

### Create the Amazon VPC endpoints

Complete the following steps to create the required Amazon VPC endpoints for your environment.

1. Sign in to the AWS Management Console using `Owner`, the open [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose **Security groups** from the left navigation panel, then create a new security group in the shared
   Amazon VPC using the following inbound, and outbound, rules:

|              | Type        | Protocol    | Source type                      | Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ----------- | ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- |
| **Inbound**  | All traffic | All         | All                              | Your environment security group                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Outbound** | All traffic | All         | All                              | `0.0.0.0/0`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | ###### Warning The `Owner` account must set up a security group in the `Owner` account to allow traffic from the new environment to the shared Amazon VPC. You can do this by creating a new security group in `Owner`, or editing an existing one. 3. Choose **Endpoints**, then create new endpoints for the environment database and the webserver (if in private mode) using the endpoint service names from the previous steps. Choose the shared Amazon VPC, the subnets you used for the environment, and the environment's security group. If successful, the environment will change from `PENDING` back to `CREATING`, then finally to `AVAILABLE`. When it is `AVAILABLE`, you can sign in to the Apache Airflow console. ### Shared Amazon VPC Troubleshooting Use the following reference to resolve issues you encounter when creating environments in a shared Amazon VPC. **Environment in `CREATE_FAILED` after `PENDING` status** <br>• Verify that `Owner` is sharing the subnets with `Participant` using [AWS Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md"). <br>• Verify that the Amazon VPC endpoints for the database and webserver are created in the same subnets associated with the environment. <br>• Verify that the security group used with your endpoints allows traffic from the security groups used for the environment. The `Owner` account creates rules that reference the security group in `Participant` as ``123456789012`/`security-group-id``:. |
| Type         | Protocol    | Source type | Source                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | --- | --- | --- |
| All traffic  | All         | All         | `123456789012`/`sg-0909e8e81919` | For more information, refer to [Responsibilities and permissions for owners and participants](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations") **Environment stuck in `PENDING` status** Verify each VPC endpoint status to ensure it is `Available`. If you configure an environment with a private webserver, you must also create an endpoint for the webserver. If the environment is stuck in `PENDING`, this might indicate that the private webserver endpoint is missing. **Received `The Vpc Endpoint Service '`vpce-service-name`' does not exist` error** If you refer to the following error, verify that the account creating the endpoints in the `Owner` account that owns the shared VPC: `ClientError: An error occurred (InvalidServiceName) when calling the CreateVpcEndpoint operation: The Vpc Endpoint Service 'vpce-service-name' does not exist` |
