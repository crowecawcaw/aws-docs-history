# Test setup with Amazon EC2

This setup demonstrates a AWS Management Console Private Access connection to Amazon Simple Storage Service from an
Amazon EC2 instance. The example uses CloudFormation to create the network configuration, and connects
to the Amazon EC2 Windows instance through Fleet Manager (a capability of AWS Systems Manager) using the
Remote Desktop Protocol (RDP).

The following diagram describes the workflow for using Amazon EC2 to access an AWS Management Console
Private Access setup. It shows how a user is connected to Amazon S3 using a private
endpoint.

![The setup configuration for trying out AWS Management Console Private Access using an Amazon EC2.](images/vpce-ec2-how-to-1.png)
Copy the following CloudFormation template and save it to a file that you will use in step three
of the _To set up a network_ procedure.

```
Description: |
  AWS Management Console Private Access.
Parameters:
  VpcCIDR:
    Type: String
    Default: 172.16.0.0/16
    Description: CIDR range for VPC
  PrivateSubnet1CIDR:
    Type: String
    Default: 172.16.1.0/24
    Description: CIDR range for Private Subnet 1
  PrivateSubnet2CIDR:
    Type: String
    Default: 172.16.2.0/24
    Description: CIDR range for Private Subnet 2
  Ec2KeyPair:
    Type: AWS::EC2::KeyPair::KeyName
    Description: The EC2 KeyPair to use to connect to the Windows instance
  LatestWindowsAmiId:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base
  InstanceTypeParameter:
    Type: String
    Default: m5.large
Resources:

  #########################
  # VPC AND SUBNETS
  #########################

  AppVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCIDR
      InstanceTenancy: default
      EnableDnsSupport: true
      EnableDnsHostnames: true

  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref AppVPC
      CidrBlock: !Ref PrivateSubnet1CIDR
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref AppVPC
      CidrBlock: !Ref PrivateSubnet2CIDR
      AvailabilityZone:
        Fn::Select:
          - 1
          - Fn::GetAZs: ""

  #########################
  # Route Tables
  #########################

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref AppVPC

  PrivateSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable
      SubnetId: !Ref PrivateSubnet1

  PrivateSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref PrivateRouteTable
      SubnetId: !Ref PrivateSubnet2

  #########################
  # SECURITY GROUPS
  #########################

  VPCEndpointSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow TLS for VPC Endpoint
      VpcId: !Ref AppVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: !GetAtt AppVPC.CidrBlock

  EC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Default EC2 Instance SG
      VpcId: !Ref AppVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 3389
          ToPort: 3389
          CidrIp: !Ref VpcCIDR

  #########################
  # VPC ENDPOINTS
  #########################

  VPCEndpointInterfaceSsm:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ssm
      VpcId: !Ref AppVPC
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC
          - Effect: Deny
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringNotEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC

  VPCEndpointInterfaceEc2Messages:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ec2messages
      VpcId: !Ref AppVPC
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC
          - Effect: Deny
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringNotEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC

  VPCEndpointInterfaceSsmMessages:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.ssmmessages
      VpcId: !Ref AppVPC
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC
          - Effect: Deny
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringNotEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC

  VPCEndpointInterfaceSignin:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.signin
      VpcId: !Ref AppVPC
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action: signin:Authenticate
            Resource: '*'
            Condition:
              StringEquals:
                aws:ResourceAccount: !Ref AWS::AccountId
          - Effect: Allow
            Principal: '*'
            Action:
              - signin:AuthorizeOAuth2Access
              - signin:CreateOAuth2Token
            Resource: '*'
            Condition:
              StringEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId

  VPCEndpointInterfaceConsole:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.console
      VpcId: !Ref AppVPC
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC
          - Effect: Deny
            Principal: '*'
            Action: '*'
            Resource: '*'
            Condition:
              StringNotEquals:
                aws:PrincipalAccount: !Ref AWS::AccountId
                aws:ResourceAccount: !Ref AWS::AccountId
                aws:SourceVpc: !Ref AppVPC

  VPCEndpointInterfaceConsoleStatic:
  # console-static only supports the full access endpoint policy
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcEndpointType: Interface
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref VPCEndpointSecurityGroup
      ServiceName: !Sub com.amazonaws.${AWS::Region}.console-static
      VpcId: !Ref AppVPC

  #########################
  # EC2 INSTANCE
  #########################

  Ec2InstanceRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore

  Ec2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref Ec2InstanceRole

  Ec2LaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateData:
        MetadataOptions:
          HttpTokens: required

  EC2WinInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestWindowsAmiId
      IamInstanceProfile: !Ref Ec2InstanceProfile
      KeyName: !Ref Ec2KeyPair
      InstanceType: !Ref InstanceTypeParameter
      SubnetId: !Ref PrivateSubnet1
      SecurityGroupIds:
        - !Ref EC2SecurityGroup
      BlockDeviceMappings:
        - DeviceName: /dev/sda1
          Ebs:
            VolumeSize: 50
      LaunchTemplate:
        LaunchTemplateId: !Ref Ec2LaunchTemplate
        Version: !GetAtt Ec2LaunchTemplate.LatestVersionNumber
      Tags:
        - Key: Name
          Value: Console VPCE test instance

```

###### To set up a network

1. Sign in to the management account for your organization and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
2. Choose **Create stack**.
3. Choose **With new resources (standard)**. Upload the CloudFormation template
   file that you previously created, and choose **Next**.
4. Enter a name for the stack, such as
   `PrivateConsoleNetworkForS3`, then choose
   **Next**.
5. For **VPC and subnets**, enter your preferred IP CIDR ranges, or
   use the provided default values. If you use the default values, verify that they don’t
   overlap with existing VPC resources in your AWS account.
6. For the **Ec2KeyPair** parameter, select one from the existing
   Amazon EC2 key pairs in your account. If you don't have an existing Amazon EC2 key pair, you must
   create one before proceeding to the next step. For more information, see [Create a key pair using Amazon EC2](../../../AWSEC2/latest/UserGuide/create-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/UserGuide/create-key-pairs.md#having-ec2-create-your-key-pair") in the
   _Amazon EC2 User Guide_.
7. Choose **Create stack**.
8. After the stack is created, choose the **Resources** tab to view
   the resources that have been created.

###### To connect to the Amazon EC2 instance

1. Sign in to the management account for your organization and open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Instances**.
3. On the **Instances** page, select **Console VPCE test
   instance** that was created by the CloudFormation template. Then choose
   **Connect**.

###### Note

This example uses Fleet Manager, a capability of AWS Systems Manager Explorer, to connect to your
Windows Server. It might take a few minutes before the connection can be
started. 4. On the **Connect to instance** page, choose **RDP
Client**, then **Connect using Fleet Manager**. 5. Choose **Fleet Manager Remote Desktop**. 6. To get the administrative password for the Amazon EC2 instance and access the Windows
Desktop using the web interface, use the private key associated with the Amazon EC2 key pair
that you used when creating the CloudFormation template . 7. From the Amazon EC2 Windows instance, open the AWS Management Console in the browser. 8. After you sign in with your AWS credentials, open the [Amazon S3 console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3") and verify that you are connected using AWS Management Console
Private Access.

###### To test AWS Management Console Private Access setup

1. Sign in to the management account for your organization and open the [Amazon S3 console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3").
2. Choose the lock-private icon in the navigation bar to view the VPC endpoint in use.
   The following screenshot shows the location of the lock-private icon and the VPC
   information.

![The Amazon S3 console showing the lock icon and AWS Management Console Private Access information.](images/console-private-access-verify-1.png)
