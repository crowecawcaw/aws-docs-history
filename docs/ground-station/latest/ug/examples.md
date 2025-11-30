# Public broadcast satellite utilizing AWS Ground Station Agent (wideband)

This example builds off the analysis done in the [JPSS-1 - Public broadcast satellite (PBS) -
Evaluation](examples.md#examples.pbs-definition "examples.md#examples.pbs-definition") section of the user guide.

To complete this example, you'll need to assume a scenario -- you want to capture
the HRD communication path as wideband digital intermediate frequency (DigIF) and process it as
it's received by the AWS Ground Station Agent on an Amazon EC2 instance using an SDR.

###### Note

The actual JPSS HRD communication path signal has a bandwidth of 30 MHz, but you will configure
the _antenna-downlink_ config to treat it as a signal with a 100 MHz
bandwidth so that it can flow through the correct path to be received by the AWS Ground Station Agent for
this example.

## Communication paths

This section represents
[Plan your dataflow communication paths](getting-started.md "getting-started.md")
of getting started. For this example, you will need an additional section in your CloudFormation template that hasn't been used in the other examples, the Mappings section.

###### Note

For more information about the contents of a CloudFormation template, see
[Template sections](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md").

You'll begin by setting up a Mappings section in your CloudFormation template for the AWS Ground Station prefix lists by region. This allows the prefix lists to be easily
referenced by the Amazon EC2 instance security group.
For more information about using a prefix list, see
[VPC Configuration with AWS Ground Station Agent](dataflows.md#dataflows.vpc-configuration.agent "dataflows.md#dataflows.vpc-configuration.agent").

```

Mappings:
  PrefixListId:
    us-east-2:
      groundstation: pl-087f83ba4f34e3bea
    us-west-2:
      groundstation: pl-0cc36273da754ebdc
    us-east-1:
      groundstation: pl-0e5696d987d033653
    eu-central-1:
      groundstation: pl-03743f81267c0a85e
    sa-east-1:
      groundstation: pl-098248765e9effc20
    ap-northeast-2:
      groundstation: pl-059b3e0b02af70e4d
    ap-southeast-1:
      groundstation: pl-0d9b804fe014a6a99
    ap-southeast-2:
      groundstation: pl-08d24302b8c4d2b73
    me-south-1:
      groundstation: pl-02781422c4c792145
    eu-west-1:
      groundstation: pl-03fa6b266557b0d4f
    eu-north-1:
      groundstation: pl-033e44023025215c0
    af-south-1:
      groundstation: pl-0382d923a9d555425

```

For the Parameters section, you're going to add the following parameters. You'll specify values for these when creating the stack via the CloudFormation console.

```

Parameters:
  EC2Key:
    Description: The SSH key used to access the EC2 receiver instance. Choose any SSH key if you are not creating an EC2 receiver instance. For instructions on how to create an SSH key see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  AZ:
    Description: "The AvailabilityZone that the resources of this stack will be created in. (e.g. us-east-2a)"
    Type: AWS::EC2::AvailabilityZone::Name

  ReceiverAMI:
    Description: The Ground Station Agent AMI ID you want to use. Please note that AMIs are region specific. For instructions on how to retrieve an AMI see https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.ec2-configuration.html#dataflows.ec2-configuration.amis
    Type: AWS::EC2::Image::Id

```

###### Note

You **need** to create a key pair, and provide the name for the Amazon EC2 `EC2Key` parameter. See
[Create a key pair for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md").

Additionally, you'll **need** to provide the correct **region specific** AMI ID, when creating the CloudFormation stack. See
[AWS Ground Station Amazon Machine Images (AMIs)](dataflows.md#dataflows.ec2-configuration.amis "dataflows.md#dataflows.ec2-configuration.amis").

The remaining template snippets belong in the Resources section of the CloudFormation
template.

```

Resources:
  # Resources that you would like to create should be placed within the Resources section.

```

Given our scenario to deliver a single communication path to an Amazon EC2 instance, you know that you'll
have a single synchronous delivery path. Per the
[Synchronous data delivery](getting-started.md#getting-started.step2.sync-data-delivery "getting-started.md#getting-started.step2.sync-data-delivery")
section, you must set up and configure an Amazon EC2 instance with AWS Ground Station Agent, and create one
or more dataflow endpoint groups. You'll begin by first setting up the Amazon VPC for the AWS Ground Station Agent.

```

  ReceiverVPC:
    Type: AWS::EC2::VPC
    Properties:
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
      CidrBlock: 10.0.0.0/16
      Tags:
      - Key: "Name"
        Value: "AWS Ground Station Example - PBS to AWS Ground Station Agent VPC"
      - Key: "Description"
        Value: "VPC for EC2 instance receiving AWS Ground Station data"

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref ReceiverVPC
      MapPublicIpOnLaunch: 'true'
      AvailabilityZone: !Ref AZ
      CidrBlock: 10.0.0.0/20
      Tags:
      - Key: "Name"
        Value: "AWS Ground Station Example - PBS to AWS Ground Station Agent Public Subnet"
      - Key: "Description"
        Value: "Subnet for EC2 instance receiving AWS Ground Station data"

  RouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref ReceiverVPC
      Tags:
        - Key: Name
          Value: AWS Ground Station Example - RouteTable

  RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTable
      SubnetId: !Ref PublicSubnet

  Route:
    Type: AWS::EC2::Route
    DependsOn: InternetGateway
    Properties:
      RouteTableId: !Ref RouteTable
      DestinationCidrBlock: '0.0.0.0/0'
      GatewayId: !Ref InternetGateway

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: AWS Ground Station Example - Internet Gateway

  GatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref ReceiverVPC
      InternetGatewayId: !Ref InternetGateway

```

###### Note

For more information about the VPC configurations supported by the AWS Ground Station Agent, see [AWS Ground Station Agent Requirements - VPC diagrams](../gs-agent-ug/agent-requirements.md#vpc-subnet-diagrams "../gs-agent-ug/agent-requirements.md#vpc-subnet-diagrams").

Next, you'll set up the Receiver Amazon EC2 instance.

```

  # The placement group in which your EC2 instance is placed.
  ClusterPlacementGroup:
    Type: AWS::EC2::PlacementGroup
    Properties:
      Strategy: cluster

  # This is required for the EIP if the receiver EC2 instance is in a private subnet.
  # This ENI must exist in a public subnet, be attached to the receiver and be associated with the EIP.
  ReceiverInstanceNetworkInterface:
    Type: AWS::EC2::NetworkInterface
    Properties:
      Description: Floating network interface
      GroupSet:
        - !Ref InstanceSecurityGroup
      SubnetId: !Ref PublicSubnet

  # An EIP providing a fixed IP address for AWS Ground Station to connect to. Attach it to the receiver instance created in the stack.
  ReceiverInstanceElasticIp:
    Type: AWS::EC2::EIP
    Properties:
      Tags:
        - Key: Name
          Value: !Join [ "-" , [ "EIP" , !Ref "AWS::StackName" ] ]

  # Attach the ENI to the EC2 instance if using a separate public subnet.
  # Requires the receiver instance to be in a public subnet (SubnetId should be the id of a public subnet)
  ReceiverNetworkInterfaceAttachment:
    Type: AWS::EC2::NetworkInterfaceAttachment
    Properties:
      DeleteOnTermination: false
      DeviceIndex: 1
      InstanceId: !Ref ReceiverInstance
      NetworkInterfaceId: !Ref ReceiverInstanceNetworkInterface

  # Associate EIP with the ENI if using a separate public subnet for the ENI.
  ReceiverNetworkInterfaceElasticIpAssociation:
    Type: AWS::EC2::EIPAssociation
    Properties:
      AllocationId: !GetAtt [ReceiverInstanceElasticIp, AllocationId]
      NetworkInterfaceId: !Ref ReceiverInstanceNetworkInterface

  # The EC2 instance that will send/receive data to/from your satellite using AWS Ground Station.
  ReceiverInstance:
    Type: AWS::EC2::Instance
    DependsOn: PublicSubnet
    Properties:
      DisableApiTermination: false
      IamInstanceProfile: !Ref GeneralInstanceProfile
      ImageId: !Ref ReceiverAMI
      AvailabilityZone: !Ref AZ
      InstanceType: c5.24xlarge
      KeyName: !Ref EC2Key
      Monitoring: true
      PlacementGroupName: !Ref ClusterPlacementGroup
      SecurityGroupIds:
        - Ref: InstanceSecurityGroup
      SubnetId: !Ref PublicSubnet
      Tags:
        - Key: Name
          Value: !Join [ "-" , [ "Receiver" , !Ref "AWS::StackName" ] ]
      # agentCpuCores list in the AGENT_CONFIG below defines the cores that the AWS Ground Station Agent is allowed to run on. This list can be changed to suit your use-case, however if the agent isn't supplied with enough cores data loss may occur.
      UserData:
        Fn::Base64:
          Fn::Sub:
            - |
              #!/bin/bash
              yum -y update

              AGENT_CONFIG_PATH="/opt/aws/groundstation/etc/aws-gs-agent-config.json"
              cat << AGENT_CONFIG > "$AGENT_CONFIG_PATH"
              {
                "capabilities": [
                  "arn:aws:groundstation:${AWS::Region}:${AWS::AccountId}:dataflow-endpoint-group/${DataflowEndpointGroupId}"
                ],
                "device": {
                  "privateIps": [
                    "127.0.0.1"
                  ],
                  "publicIps": [
                    "${EIP}"
                  ],
                  "agentCpuCores": [
                    24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92
                  ]
                }
              }
              AGENT_CONFIG

              systemctl start aws-groundstation-agent
              systemctl enable aws-groundstation-agent

              # <Tuning Section Start>
              # Visit the AWS Ground Station Agent Documentation in the User Guide for more details and guidance updates

              # Set IRQ affinity with list of CPU cores and Receive Side Scaling mask
              # Core list should be the first two cores (and hyperthreads) on each socket
              # Mask set to everything currently
              # https://github.com/torvalds/linux/blob/v4.11/Documentation/networking/scaling.txt#L80-L96
              echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '0 1 48 49' 'ffffffff,ffffffff,ffffffff' >>/var/log/user-data.log 2>&1" >>/var/spool/cron/root

              # Reserving the port range defined in the GS agent ingress address in the Dataflow Endpoint Group so the kernel doesn't steal any of them from the GS agent. These ports are the ports that the GS agent will ingress data
              # across, so if the kernel steals one it could cause problems ingressing data onto the instance.
              echo net.ipv4.ip_local_reserved_ports="42000-50000" >> /etc/sysctl.conf

              # </Tuning Section End>

              # We have to reboot for linux kernel settings to apply
              shutdown -r now

            - DataflowEndpointGroupId: !Ref DataflowEndpointGroup
              EIP: !Ref ReceiverInstanceElasticIp

```

```

  # The AWS Ground Station Dataflow Endpoint Group that defines the endpoints that AWS Ground
  # Station will use to send/receive data to/from your satellite.
  DataflowEndpointGroup:
    Type: AWS::GroundStation::DataflowEndpointGroup
    Properties:
      ContactPostPassDurationSeconds: 180
      ContactPrePassDurationSeconds: 120
      EndpointDetails:
        - AwsGroundStationAgentEndpoint:
            Name: !Join [ "-" , [ !Ref "AWS::StackName" , "Downlink" ] ] # needs to match DataflowEndpointConfig name
            EgressAddress:
              SocketAddress:
                Name: 127.0.0.1
                Port: 55000
            IngressAddress:
              SocketAddress:
                Name: !Ref ReceiverInstanceElasticIp
                PortRange:
                  Minimum: 42000
                  Maximum: 55000

```

You'll also need the appropriate policies, roles, and profiles to allow AWS Ground Station to create the elastic network interface (ENI) in
your account.

```

  # The security group for your EC2 instance.
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: AWS Ground Station receiver instance security group.
      VpcId: !Ref ReceiverVPC
      SecurityGroupEgress:
        - CidrIp: 0.0.0.0/0
          Description: Allow all outbound traffic by default
          IpProtocol: "-1"
      SecurityGroupIngress:
        # To allow SSH access to the instance, add another rule allowing tcp port 22 from your CidrIp
        - IpProtocol: udp
          Description: Allow AWS Ground Station Incoming Dataflows
          ToPort: 50000
          FromPort: 42000
          SourcePrefixListId:
            Fn::FindInMap:
              - PrefixListId
              - Ref: AWS::Region
              - groundstation

   # The EC2 instance assumes this role.
  InstanceRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "ec2.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
        - arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role
        - arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
        - arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM
        - arn:aws:iam::aws:policy/AWSGroundStationAgentInstancePolicy
      Policies:
        - PolicyDocument:
            Statement:
              - Action:
                  - sts:AssumeRole
                Effect: Allow
                Resource: !GetAtt GroundStationKmsKeyRole.Arn
            Version: "2012-10-17"
          PolicyName: InstanceGroundStationApiAccessPolicy

  # The instance profile for your EC2 instance.
  GeneralInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - !Ref InstanceRole

  # The IAM role that AWS Ground Station will assume to access and use the KMS Key for data delivery
  GroundStationKmsKeyRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - groundstation.amazonaws.com
            Condition:
              StringEquals:
                "aws:SourceAccount": !Ref AWS::AccountId
              ArnLike:
                "aws:SourceArn": !Sub "arn:${AWS::Partition}:groundstation:${AWS::Region}:${AWS::AccountId}:mission-profile/*"
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              AWS: !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"

  GroundStationKmsKeyAccessPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - kms:Decrypt
            Effect: Allow
            Resource: !GetAtt GroundStationDataDeliveryKmsKey.Arn
      PolicyName: GroundStationKmsKeyAccessPolicy
      Roles:
        - Ref: GroundStationKmsKeyRole

  GroundStationDataDeliveryKmsKey:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Statement:
          - Action:
              - kms:CreateAlias
              - kms:Describe*
              - kms:Enable*
              - kms:List*
              - kms:Put*
              - kms:Update*
              - kms:Revoke*
              - kms:Disable*
              - kms:Get*
              - kms:Delete*
              - kms:ScheduleKeyDeletion
              - kms:CancelKeyDeletion
              - kms:GenerateDataKey
              - kms:TagResource
              - kms:UntagResource
            Effect: Allow
            Principal:
              AWS: !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
            Resource: "*"
          - Action:
              - kms:Decrypt
              - kms:GenerateDataKeyWithoutPlaintext
            Effect: Allow
            Principal:
              AWS: !GetAtt GroundStationKmsKeyRole.Arn
            Resource: "*"
            Condition:
              StringEquals:
                "kms:EncryptionContext:sourceAccount": !Ref AWS::AccountId
              ArnLike:
                "kms:EncryptionContext:sourceArn": !Sub "arn:${AWS::Partition}:groundstation:${AWS::Region}:${AWS::AccountId}:mission-profile/*"
          - Action:
              - kms:CreateGrant
            Effect: Allow
            Principal:
              AWS: !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:root"
            Resource: "*"
            Condition:
              ForAllValues:StringEquals:
                "kms:GrantOperations":
                  - Decrypt
                  - GenerateDataKeyWithoutPlaintext
                "kms:EncryptionContextKeys":
                  - sourceArn
                  - sourceAccount
              ArnLike:
                "kms:EncryptionContext:sourceArn": !Sub "arn:${AWS::Partition}:groundstation:${AWS::Region}:${AWS::AccountId}:mission-profile/*"
              StringEquals:
                "kms:EncryptionContext:sourceAccount": !Ref AWS::AccountId
        Version: "2012-10-17"
      EnableKeyRotation: true

```

## AWS Ground Station configs

This section represents
[Create configs](getting-started.md "getting-started.md")
of getting started.

You'll need a _tracking-config_ to set your preference on using
autotrack. Selecting _PREFERRED_ as autotrack can improve the signal
quality, but it isn't required to meet the signal quality due to sufficient JPSS-1 ephemeris
quality.

```

  TrackingConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "JPSS Tracking Config"
      ConfigData:
        TrackingConfig:
          Autotrack: "PREFERRED"

```

Based on the communication path, you'll need to define an
_antenna-downlink_ config to represent the satellite portion, as well as a
_dataflow-endpoint_ config to refer to the dataflow endpoint group that
defines the endpoint details.

```

  # The AWS Ground Station Antenna Downlink Config that defines the frequency spectrum used to
  # downlink data from your satellite.
  SnppJpssDownlinkDigIfAntennaConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "SNPP JPSS Downlink WBDigIF Antenna Config"
      ConfigData:
        AntennaDownlinkConfig:
          SpectrumConfig:
            Bandwidth:
              Units: "MHz"
              Value: 100
            CenterFrequency:
              Units: "MHz"
              Value: 7812
            Polarization: "RIGHT_HAND"

  # The AWS Ground Station Dataflow Endpoint Config that defines the endpoint used to downlink data
  # from your satellite.
  DownlinkDigIfEndpointConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "Aqua SNPP JPSS Terra Downlink DigIF Endpoint Config"
      ConfigData:
        DataflowEndpointConfig:
          DataflowEndpointName: !Join [ "-" , [ !Ref "AWS::StackName" , "Downlink" ] ]
          DataflowEndpointRegion: !Ref AWS::Region

```

## AWS Ground Station mission profile

This section represents
[Create mission profile](getting-started.md "getting-started.md") of getting started.

Now that you have the associated configs, you can use them to construct the dataflow. You'll use
the defaults for the remaining parameters.

```

  # The AWS Ground Station Mission Profile that groups the above configurations to define how to
  # uplink and downlink data to your satellite.
  SnppJpssMissionProfile:
    Type: AWS::GroundStation::MissionProfile
    Properties:
      Name: !Sub 'JPSS WBDigIF gs-agent EC2 Delivery'
      ContactPrePassDurationSeconds: 120
      ContactPostPassDurationSeconds: 120
      MinimumViableContactDurationSeconds: 180
      TrackingConfigArn: !Ref TrackingConfig
      DataflowEdges:
        - Source: !Ref SnppJpssDownlinkDigIfAntennaConfig
          Destination: !Ref DownlinkDigIfEndpointConfig
      StreamsKmsKey:
        KmsKeyArn: !GetAtt GroundStationDataDeliveryKmsKey.Arn
      StreamsKmsRole: !GetAtt GroundStationKmsKeyRole.Arn

```

## Putting it together

With the above resources, you now have the ability to schedule JPSS-1 contacts for
synchronous data delivery from any of your onboarded AWS Ground Station [AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md").

The following is a complete CloudFormation template that includes all resources described
in this section combined into a single template that can be directly used in CloudFormation.

The CloudFormation template named `DirectBroadcastSatelliteWbDigIfEc2DataDelivery.yml` is
designed to give you quick access to start receiving digitized intermediate frequency (DigIF)
data for the Aqua, SNPP, JPSS-1/NOAA-20, and Terra satellites.
It contains an Amazon EC2 instance and the required CloudFormation resources to receive raw DigIF direct
broadcast data using AWS Ground Station Agent.

If Aqua, SNPP, JPSS-1/NOAA-20, and Terra are not onboarded to your account, see
[Onboard satellite](getting-started.md "getting-started.md").

###### Note

You can access the template by accessing the customer onboarding Amazon S3 bucket using valid
AWS credentials. The links below use a regional Amazon S3 bucket.
Change the `us-west-2` region code to represent the corresponding region of which you want to create the CloudFormation
stack in.

Additionally, the following instructions use YAML. However, the templates are available in
both YAML and JSON format. To use JSON, replace the `.yml` file extension with
`.json` when downloading the template.

To download the template using AWS CLI, use the following command:

```
aws s3 cp s3://groundstation-cloudformation-templates-us-west-2/agent/ec2_delivery/DirectBroadcastSatelliteWbDigIfEc2DataDelivery.yml .
```

You can view and download the template in the console by navigating to the following URL in
your browser:

```
https://s3.console.aws.amazon.com/s3/object/groundstation-cloudformation-templates-us-west-2/agent/ec2_delivery/DirectBroadcastSatelliteWbDigIfEc2DataDelivery.yml
```

You can specify the template directly in CloudFormation using the following link:

```
https://groundstation-cloudformation-templates-us-west-2.s3.us-west-2.amazonaws.com/agent/ec2_delivery/DirectBroadcastSatelliteWbDigIfEc2DataDelivery.yml
```

**What additional resources does the template define?**

The `DirectBroadcastSatelliteWbDigIfEc2DataDelivery` template includes the following additional resources:

- **Receiver Instance Elastic Network Interface**

* (Conditional) An elastic network interface is created in the subnet specified by **PublicSubnetId** if provided. This is required if the receiver instance is in a private subnet.
  The elastic network interface will be associated with the EIP and attached to the receiver
  instance.

- **Receiver Instance Elastic IP**

* An elastic IP that AWS Ground Station will connect to.
  This attaches to the receiver instance or elastic network interface.

- One of the following Elastic IP associations:
  - **Receiver Instance to Elastic IP Association**
  * The association of the Elastic IP to your receiver instance, if **PublicSubnetId** is not specified. This requires that **SubnetId** reference a public subnet.
  - **Receiver Instance Elastic Network Interface to Elastic IP
    Association**
  * The association of the elastic IP to the receiver instance elastic network
    interface, if **PublicSubnetId** is specified.

- (Optional) **CloudWatch Event Triggers** - AWS Lambda
  Function that is triggered using CloudWatch Events sent by AWS Ground Station before and after a contact.
  The AWS Lambda Function will start and optionally stop your Receiver Instance.
- (Optional) **Amazon EC2 Verification for Contacts** - The option
  to use Lambda to set up a verification system of your Amazon EC2 instance(s) for contacts
  with SNS notification. It is important to note that this may incur charges depending on
  your current usage.
- **Additional mission profiles**

* Mission profiles for additional public broadcast satellites (Aqua, SNPP, and Terra).

- **Additional antenna-downlink configs**

* Antenna downlink configs for additional public broadcast satellites (Aqua, SNPP, and
  Terra).

The values and parameters for the satellites in this template are already populated. These
parameters make it easy for you to use AWS Ground Station immediately with these satellites.
You do not need to configure your own values in order to use AWS Ground Station when using this template.
However, you can customize the values to make the template work for your use case.

**Where do I receive my data?**

The dataflow endpoint group is set up to use the receiver instance network interface that
part of the template creates.
The receiver instance uses the AWS Ground Station Agent to receive the data stream from AWS Ground Station on the port
defined by the dataflow endpoint.
For more information about setting up a dataflow endpoint group, see
[AWS::GroundStation::DataflowEndpointGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md"). For more information about the AWS Ground Station
Agent, see
[What is the AWS Ground Station Agent?](../gs-agent-ug/overview.md "../gs-agent-ug/overview.md")
