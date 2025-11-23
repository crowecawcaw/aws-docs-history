# Create a VPC network

Creating a VPC network is **optional** with Amazon MWAA Serverless. This section describes the different options you can use if you choose to create a Amazon VPC network.

To learn how to manage access to your VPC, refer to [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").

###### Tip

Apache Airflow works best in a low-latency network environment. If you are using an existing Amazon VPC which routes traffic to another region or to an on-premise environment, we recommended adding AWS PrivateLink endpoints for CloudWatch and AWS KMS. For more information about configuring AWS PrivateLink for Amazon MWAA Serverless, refer to [Access Amazon MWAA Serverless using an interface endpoint (AWS PrivateLink)](networking-privatelink.md "networking-privatelink.md").

## Prerequisites

The AWS Command Line Interface (AWS CLI) is an open source tool that enables you to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:

- [Install AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").
- [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

## Create your Amazon VPC network

You have the following options to create a Amazon VPC network:

- [Create an Amazon VPC network with internet access](#create-vpc-template-private-public "#create-vpc-template-private-public")
- [Create an Amazon VPC network without internet access](#create-vpc-template-private "#create-vpc-template-private")

###### Note

Amazon MWAA Serverless does not support the use of `use1-az3` Availability Zone (AZ) in the US East (N. Virginia) Region. When creating the VPC for Amazon MWAA Serverless in the US East (N. Virginia) region, you must explicitly assign the `AvailabilityZone` in the CloudFormation en(CFN) template. The assigned availability zone name must not be mapped to `use1-az3`. You can retrieve the detailed mapping of AZ names to their corresponding AZ IDs by running the following command:

```
aws ec2 describe-availability-zones --region us-east-1
```

For more information about VPCs and networking, refer to [Get started with AWS PrivateLink](../../../vpc/latest/privatelink/getting-started.md "../../../vpc/latest/privatelink/getting-started.md") in the AWS PrivateLink User Guide.

The following CloudFormation template creates an Amazon VPC network _with internet access_ in your default AWS Region. This option uses public routing over the internet. This template can be used for an Apache Airflow _Web server_ with the **Private network** or **Public network** access modes.

1. Copy the contents of the following template and save locally as `cfn-vpc-public-private.yaml`.

```
Description:  This template deploys a VPC, with a pair of public and private subnets spread
  across two Availability Zones. It deploys an internet gateway, with a default
  route on the public subnets. It deploys a pair of NAT gateways (one in each AZ),
  and default routes for them in the private subnets.

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
    Description: Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone
    Type: String
    Default: 10.192.10.0/24

  PublicSubnet2CIDR:
    Description: Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone
    Type: String
    Default: 10.192.11.0/24

  PrivateSubnet1CIDR:
    Description: Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone
    Type: String
    Default: 10.192.20.0/24

  PrivateSubnet2CIDR:
    Description: Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone
    Type: String
    Default: 10.192.21.0/24

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCIDR
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: !Ref EnvironmentName

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: !Ref EnvironmentName

  InternetGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      InternetGatewayId: !Ref InternetGateway
      VpcId: !Ref VPC

  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: !Ref PublicSubnet1CIDR
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Public Subnet (AZ1)

  PublicSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs  '' ]
      CidrBlock: !Ref PublicSubnet2CIDR
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Public Subnet (AZ2)

  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs  '' ]
      CidrBlock: !Ref PrivateSubnet1CIDR
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Private Subnet (AZ1)

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs  '' ]
      CidrBlock: !Ref PrivateSubnet2CIDR
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Private Subnet (AZ2)

  NatGateway1EIP:
    Type: AWS::EC2::EIP
    DependsOn: InternetGatewayAttachment
    Properties:
      Domain: vpc

  NatGateway2EIP:
    Type: AWS::EC2::EIP
    DependsOn: InternetGatewayAttachment
    Properties:
      Domain: vpc

  NatGateway1:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGateway1EIP.AllocationId
      SubnetId: !Ref PublicSubnet1

  NatGateway2:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatGateway2EIP.AllocationId
      SubnetId: !Ref PublicSubnet2

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Public Routes

  DefaultPublicRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  PublicSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet1

  PublicSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicSubnet2


  PrivateRouteTable1:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Private Routes (AZ1)

  DefaultPrivateRoute1:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable1
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway1

  PrivateSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable1
      SubnetId: !Ref PrivateSubnet1

  PrivateRouteTable2:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName} Private Routes (AZ2)

  DefaultPrivateRoute2:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway2

  PrivateSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable2
      SubnetId: !Ref PrivateSubnet2

  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: "mwaa-security-group"
      GroupDescription: "Security group with a self-referencing inbound rule."
      VpcId: !Ref VPC

  SecurityGroupIngress:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref SecurityGroup
      IpProtocol: "-1"
      SourceSecurityGroupId: !Ref SecurityGroup

Outputs:
  VPC:
    Description: A reference to the created VPC
    Value: !Ref VPC

  PublicSubnets:
    Description: A list of the public subnets
    Value: !Join [ ",", [ !Ref PublicSubnet1, !Ref PublicSubnet2 ]]

  PrivateSubnets:
    Description: A list of the private subnets
    Value: !Join [ ",", [ !Ref PrivateSubnet1, !Ref PrivateSubnet2 ]]

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

2. In your command prompt, navigate to the directory where `cfn-vpc-public-private.yaml` is stored. For example:

```
cd mwaaproject
```

3. Use the [`aws cloudformation create-stack`](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md") command to create the stack using the AWS CLI.

```
aws cloudformation create-stack --stack-name mwaa-serverless-workflow --template-body file://cfn-vpc-public-private.yaml
```

###### Note

It takes about 30 minutes to create the Amazon VPC infrastructure.
The following CloudFormation template creates an Amazon VPC network _without internet access_ in your default AWS Region.

This option uses private routing without internet access. You can use this template for an Apache Airflow _Web server_ with **Private network** access mode only. It creates the required VPC endpoints for the AWS services that are used by a workflow. For more information, refer to [Attaching the required VPC endpoints](../userguide/vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-all "../userguide/vpc-vpe-create-access.md#vpc-vpe-create-view-endpoints-attach-all") in the Amazon MWAA User Guide.

1. Copy the contents of the following template and save locally as `cfn-vpc-private.yaml`.

```
AWSTemplateFormatVersion: "2010-09-09"

Parameters:
   VpcCIDR:
     Description: The IP range (CIDR notation) for this VPC
     Type: String
     Default: 10.192.0.0/16

   PrivateSubnet1CIDR:
     Description: The IP range (CIDR notation) for the private subnet in the first Availability Zone
     Type: String
     Default: 10.192.10.0/24

   PrivateSubnet2CIDR:
     Description: The IP range (CIDR notation) for the private subnet in the second Availability Zone
     Type: String
     Default: 10.192.11.0/24

Resources:
   VPC:
     Type: AWS::EC2::VPC
     Properties:
       CidrBlock: !Ref VpcCIDR
       EnableDnsSupport: true
       EnableDnsHostnames: true
       Tags:
        - Key: Name
          Value: !Ref AWS::StackName

   RouteTable:
     Type: AWS::EC2::RouteTable
     Properties:
       VpcId: !Ref VPC
       Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-route-table"

   PrivateSubnet1:
     Type: AWS::EC2::Subnet
     Properties:
       VpcId: !Ref VPC
       AvailabilityZone: !Select [ 0, !GetAZs  '' ]
       CidrBlock: !Ref PrivateSubnet1CIDR
       MapPublicIpOnLaunch: false
       Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName} Private Subnet (AZ1)"

   PrivateSubnet2:
     Type: AWS::EC2::Subnet
     Properties:
       VpcId: !Ref VPC
       AvailabilityZone: !Select [ 1, !GetAZs  '' ]
       CidrBlock: !Ref PrivateSubnet2CIDR
       MapPublicIpOnLaunch: false
       Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName} Private Subnet (AZ2)"

   PrivateSubnet1RouteTableAssociation:
     Type: AWS::EC2::SubnetRouteTableAssociation
     Properties:
       RouteTableId: !Ref RouteTable
       SubnetId: !Ref PrivateSubnet1

   PrivateSubnet2RouteTableAssociation:
     Type: AWS::EC2::SubnetRouteTableAssociation
     Properties:
       RouteTableId: !Ref RouteTable
       SubnetId: !Ref PrivateSubnet2

   SecurityGroup:
     Type: AWS::EC2::SecurityGroup
     Properties:
       VpcId: !Ref VPC
       GroupDescription: Security Group for Amazon MWAA Environments to access VPC endpoints
       GroupName: !Sub "${AWS::StackName}-mwaa-serverless-security-group"

   SecurityGroupIngress:
     Type: AWS::EC2::SecurityGroupIngress
     Properties:
       GroupId: !Ref SecurityGroup
       IpProtocol: "-1"
       SourceSecurityGroupId: !Ref SecurityGroup

   CloudWatchLogsVpcEndoint:
     Type: AWS::EC2::VPCEndpoint
     Properties:
       ServiceName: !Sub "com.amazonaws.${AWS::Region}.logs"
       VpcEndpointType: Interface
       VpcId: !Ref VPC
       PrivateDnsEnabled: true
       SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
       SecurityGroupIds:
        - !Ref SecurityGroup

   CloudWatchMonitoringVpcEndoint:
     Type: AWS::EC2::VPCEndpoint
     Properties:
       ServiceName: !Sub "com.amazonaws.${AWS::Region}.monitoring"
       VpcEndpointType: Interface
       VpcId: !Ref VPC
       PrivateDnsEnabled: true
       SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
       SecurityGroupIds:
        - !Ref SecurityGroup

   KmsVpcEndoint:
     Type: AWS::EC2::VPCEndpoint
     Properties:
       ServiceName: !Sub "com.amazonaws.${AWS::Region}.kms"
       VpcEndpointType: Interface
       VpcId: !Ref VPC
       PrivateDnsEnabled: true
       SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
       SecurityGroupIds:
        - !Ref SecurityGroup


Outputs:
   VPC:
     Description: A reference to the created VPC
     Value: !Ref VPC

   MwaaSecurityGroupId:
     Description: Associates the Security Group to the environment to allow access to the VPC endpoints
     Value: !Ref SecurityGroup

   PrivateSubnets:
     Description: A list of the private subnets
     Value: !Join [ ",", [ !Ref PrivateSubnet1, !Ref PrivateSubnet2 ]]

   PrivateSubnet1:
     Description: A reference to the private subnet in the 1st Availability Zone
     Value: !Ref PrivateSubnet1

   PrivateSubnet2:
     Description: A reference to the private subnet in the 2nd Availability Zone
     Value: !Ref PrivateSubnet2
```

2. In your command prompt, navigate to the directory where `cfn-vpc-private.yml` is stored. For example:

```
cd mwaaproject
```

3. Use the [`aws cloudformation create-stack`](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md") command to create the stack using the AWS CLI.

```
aws cloudformation create-stack --stack-name mwaa-serverless-private-workflow --template-body file://cfn-vpc-private.yml
```

###### Note

It takes about 30 minutes to create the Amazon VPC infrastructure. 4. You'll need to create a mechanism to access these VPC endpoints from your computer. To learn more, refer to [Managing access to service-specific Amazon VPC endpoints on Amazon MWAA](../userguide/vpc-vpe-access.md "../userguide/vpc-vpe-access.md") in the Amazon MWAA User Guide.

###### Note

You can further restrict outbound access in the CIDR of your Amazon MWAA Serverless security group. For example, you can restrict to itself by adding a self-referencing outbound rule and the CIDR of your Amazon VPC.
