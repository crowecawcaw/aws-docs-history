# Test setup with Amazon WorkSpaces

Amazon WorkSpaces enables you to provision virtual, cloud-based Windows, Amazon Linux, or Ubuntu
Linux desktops for your users, known as WorkSpaces. You can quickly add or remove users as
your needs change. Users can access their virtual desktops from multiple devices or web
browsers. To learn more about WorkSpaces, see the [Amazon WorkSpaces Administration
Guide](../../../workspaces/latest/adminguide/amazon-workspaces.md "../../../workspaces/latest/adminguide/amazon-workspaces.md").

The example in this section describes a test environment in which a user environment
uses a web browser running on a WorkSpace to sign in to AWS Management Console Private Access. Then, the
user visits the Amazon Simple Storage Service console. This WorkSpace is meant to simulate the experience of a
corporate user with a laptop on a VPC-connected network, accessing the AWS Management Console from their
browser.

This tutorial uses AWS CloudFormation to create and configure the network setup and a Simple
Active Directory to be used by WorkSpaces along with step by step instructions to setup a
WorkSpace using the AWS Management Console.

The following diagram describes the workflow for using a WorkSpace to test an AWS Management Console
Private Access setup. It shows the relationship between a client WorkSpace, an Amazon
managed VPC and a customer managed VPC.

![The setup configuration for testing a AWS Management Console Private Access using an Amazon WorkSpaces.](images/vpce-workspaces-how-to-1.png)
Copy the following CloudFormation template and save it to a file that you will use in step 3 of
the procedure to set up a network.

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
  DSAdminPasswordResourceName:
    Type: String
    Default: ADAdminSecret
    Description: Password for directory services admin
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

  #########################
  # VPC ENDPOINTS
  #########################

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
  # WORKSPACE RESOURCES
  #########################

  ADAdminSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: !Ref DSAdminPasswordResourceName
      Description: Password for directory services admin
      GenerateSecretString:
        SecretStringTemplate: '{"username": "Admin"}'
        GenerateStringKey: password
        PasswordLength: 30
        ExcludeCharacters: '"@/\'

  WorkspaceSimpleDirectory:
    Type: AWS::DirectoryService::SimpleAD
    Properties:
      Name: corp.awsconsole.com
      Password:
        Fn::Sub: "{{resolve:secretsmanager:${DSAdminPasswordResourceName}:SecretString:password}}"
      Size: Small
      VpcSettings:
        SubnetIds:
          - !Ref PrivateSubnet1
          - !Ref PrivateSubnet2
        VpcId: !Ref AppVPC
Outputs:
  PrivateSubnet1:
    Description: Private Subnet 1
    Value: !Ref PrivateSubnet1
  PrivateSubnet2:
    Description: Private Subnet 2
    Value: !Ref PrivateSubnet2
  WorkspaceSimpleDirectory:
    Description: Directory to be used for Workspaces
    Value: !Ref WorkspaceSimpleDirectory
  WorkspacesAdminPassword:
    Description: The ARN of the Workspaces admin's password. Navigate to the Secrets Manager in the AWS Console to view the value.
    Value: !Ref ADAdminSecret

```

###### Note

This test setup is designed to run in the US East (N. Virginia) (us-east-1)
Region.

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
6. Choose **Create stack**.
7. After the stack is created, choose the **Resources** tab to view
   the resources that have been created.
8. Choose the **Outputs** tab, to view the values for private subnets
   and the Workspace Simple Directory. Take note of these values, as you will use them in
   step four of the next procedure for creating and configuring a WorkSpace.
   The following screenshot shows the view of the **Outputs** tab
   displaying the values for the private subnets and the Workspace Simple Directory.

![The private subnets and Workspace Simple Directory and their corresponding values.](images/vpce-workspaces-how-to-2-latest.png)
Now that you have created your network, use the following procedures to create and
access a WorkSpace.

###### To create a WorkSpace

1. Open the [WorkSpaces console](https://console.aws.amazon.com/workspaces "https://console.aws.amazon.com/workspaces").
2. In the navigation pane, choose **Directories**.
3. On the **Directories** page, verify that the directory status is
   **Active**. The following screenshot shows a
   **Directories** page with an active directory.

![The Directories page with an entry for a directory with an active status.](images/vpce-workspaces-how-to-3-updated.png) 4. To use a directory in WorkSpaces, you must register it. In the navigation pane,
choose **WorkSpaces**, then choose **Create
WorkSpaces**. 5. For **Select a directory**, choose the directory created by CloudFormation
in the preceding procedure. On the **Actions** menu, choose
**Register**. 6. For the subnet selection, select the two private subnets noted in step nine of the
preceding procedure. 7. Select **Enable self-service permissions**, then choose
**Register**. 8. After the directory is registered, continue creating the WorkSpace. Select the
registered directory, then choose **Next**. 9. On the **Create users** page, choose **Create additional
user**. Enter your name and email to enable you to use the WorkSpace. Verify
that the email address is valid as the WorkSpace login information is sent to this email
address. 10. Choose **Next**. 11. On the **Identify Users** page, select the user you created in step
nine, then choose **Next**. 12. On the **Select Bundle** page, choose **Standard with
Amazon Linux 2**, then choose **Next**. 13. Use the default settings for the running mode and user customization, and then
choose **Create Workspace**. The WorkSpace starts out in
`Pending` status and transitions to `Available` within about 20
minutes. 14. When the WorkSpace is available, you will receive an email with instructions for
accessing it at the email address you provided in step nine.
After you sign in to your WorkSpace, you can test that you are accessing it using your
AWS Management Console Private Access.

###### To access a WorkSpace

1. Open the email that you received in step 14 of the preceding procedure.
2. In the email, choose the unique link that is provided to set up your profile and
   download the WorkSpaces client.
3. Set your password.
4. Download the client of your choice.
5. Install and launch the client. Enter the registration code that was provided in your
   email, then choose **Register**.
6. Sign in to Amazon WorkSpaces using the credentials you created in step three.

###### To test AWS Management Console Private Access setup

1. From your WorkSpace, open your browser. Then, navigate to the [AWS Management Console](https://console.aws.amazon.com/console "https://console.aws.amazon.com/console") and sign in using your credentials.

###### Note

If you are using Firefox as your browser, verify that the **Enable DNS
over HTTPS** option is turned off in your browser settings. 2. Open the [Amazon S3 console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3") where you can verify
that you are connected using AWS Management Console Private Access. 3. Choose the lock-private icon on the navigation bar to view the VPC and VPC endpoint
in use. The following screenshot shows the location of the lock-private icon and the VPC
information.

![The Amazon S3 console showing the lock-private icon location and AWS Management Console Private Access information.](/images/awsconsolehelpdocs/latest/gsg/images/console-private-access-verify-1.png)
