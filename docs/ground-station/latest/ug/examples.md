# Public broadcast satellite utilizing a dataflow endpoint (narrowband)

This example builds off the analysis done in the [JPSS-1 - Public broadcast satellite (PBS) -
Evaluation](examples.md#examples.pbs-definition "examples.md#examples.pbs-definition") section of the user guide.

To complete this example, you'll need to assume a scenario -- you want to capture
the HRD communication path as digital intermediate frequency (DigIF) and process it as it's
received by a dataflow endpoint application on an Amazon EC2 instance using an SDR.

## Communication paths

This section represents [Plan your dataflow communication paths](getting-started.md "getting-started.md") of getting started.
For this example, you will be creating two sections in your CloudFormation template: Parameters and Resources sections.

###### Note

For more information about the contents of a CloudFormation template, see
[Template sections](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md").

For the Parameters section, you're going to add the following parameters. You'll specify values for these when creating the stack via the CloudFormation console.

```

Parameters:
  EC2Key:
    Description: The SSH key used to access the EC2 receiver instance. Choose any SSH key if you are not creating an EC2 receiver instance. For instructions on how to create an SSH key see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  ReceiverAMI:
    Description: The Ground Station DDX AMI ID you want to use. Please note that AMIs are region specific. For instructions on how to retrieve an AMI see https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.ec2-configuration.html#dataflows.ec2-configuration.amis
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
  # Resources that you would like to create should be placed within the resource section.

```

Given our scenario to deliver a single communication path to an EC2 instance, you'll
have a single synchronous delivery path. Per the
[Synchronous data delivery](getting-started.md#getting-started.step2.sync-data-delivery "getting-started.md#getting-started.step2.sync-data-delivery")
section, you must set up and configure an Amazon EC2 instance with a dataflow endpoint
application, and create one or more dataflow endpoint groups.

```

  # The EC2 instance that will send/receive data to/from your satellite using AWS Ground Station.
  ReceiverInstance:
    Type: AWS::EC2::Instance
    Properties:
      DisableApiTermination: false
      IamInstanceProfile: !Ref GeneralInstanceProfile
      ImageId: !Ref ReceiverAMI
      InstanceType: m5.4xlarge
      KeyName: !Ref EC2Key
      Monitoring: true
      PlacementGroupName: !Ref ClusterPlacementGroup
      SecurityGroupIds:
        - Ref: InstanceSecurityGroup
      SubnetId: !Ref ReceiverSubnet
      BlockDeviceMappings:
        - DeviceName: /dev/xvda
          Ebs:
            VolumeType: gp2
            VolumeSize: 40
      Tags:
        - Key: Name
          Value: !Join [ "-" , [ "Receiver" , !Ref "AWS::StackName" ] ]
      UserData:
        Fn::Base64:
          |
          #!/bin/bash
          exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
          echo `date +'%F %R:%S'` "INFO: Logging Setup" >&2

          GROUND_STATION_DIR="/opt/aws/groundstation"
          GROUND_STATION_BIN_DIR="${GROUND_STATION_DIR}/bin"
          STREAM_CONFIG_PATH="${GROUND_STATION_DIR}/customer_stream_config.json"

          echo "Creating ${STREAM_CONFIG_PATH}"
          cat << STREAM_CONFIG > "${STREAM_CONFIG_PATH}"
          {
            "ddx_streams": [
              {
                "streamName": "Downlink",
                "maximumWanRate": 4000000000,
                "lanConfigDevice": "lo",
                "lanConfigPort": 50000,
                "wanConfigDevice": "eth1",
                "wanConfigPort": 55888,
                "isUplink": false
              }
            ]
          }
          STREAM_CONFIG

          echo "Waiting for dataflow endpoint application to start"
          while netstat -lnt | awk '$4 ~ /:80$/ {exit 1}'; do sleep 10; done

          echo "Configuring dataflow endpoint application streams"
          python "${GROUND_STATION_BIN_DIR}/configure_streams.py" --configFileName "${STREAM_CONFIG_PATH}"
          sleep 2
          python "${GROUND_STATION_BIN_DIR}/save_default_config.py"

          exit 0

  # The AWS Ground Station Dataflow Endpoint Group that defines the endpoints that AWS Ground
  # Station will use to send/receive data to/from your satellite.
  DataflowEndpointGroup:
    Type: AWS::GroundStation::DataflowEndpointGroup
    Properties:
      ContactPostPassDurationSeconds: 180
      ContactPrePassDurationSeconds: 120
      EndpointDetails:
        - Endpoint:
            Name: !Join [ "-" , [ !Ref "AWS::StackName" , "Downlink" ] ] # needs to match DataflowEndpointConfig name
            Address:
              Name: !GetAtt ReceiverInstanceNetworkInterface.PrimaryPrivateIpAddress
              Port: 55888
          SecurityDetails:
            SecurityGroupIds:
              - Ref: "DataflowEndpointSecurityGroup"
            SubnetIds:
              - !Ref ReceiverSubnet
            RoleArn: !GetAtt DataDeliveryServiceRole.Arn

  # The security group for your EC2 instance.
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: AWS Ground Station receiver instance security group.
      VpcId: !Ref ReceiverVPC
      SecurityGroupIngress:
        # To allow SSH access to the instance, add another rule allowing tcp port 22 from your CidrIp
        - IpProtocol: udp
          FromPort: 55888
          ToPort: 55888
          SourceSecurityGroupId: !Ref DataflowEndpointSecurityGroup
          Description: "AWS Ground Station Downlink Stream"

  # The security group that the ENI created by AWS Ground Station belongs to.
  DataflowEndpointSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Security Group for AWS Ground Station registration of Dataflow Endpoint Groups
      VpcId: !Ref ReceiverVPC
      SecurityGroupEgress:
        - IpProtocol: udp
          FromPort: 55888
          ToPort: 55888
          CidrIp: 10.0.0.0/8
          Description: "AWS Ground Station Downlink Stream To 10/8"
        - IpProtocol: udp
          FromPort: 55888
          ToPort: 55888
          CidrIp: 172.16.0.0/12
          Description: "AWS Ground Station Downlink Stream To 172.16/12"
        - IpProtocol: udp
          FromPort: 55888
          ToPort: 55888
          CidrIp: 192.168.0.0/16
          Description: "AWS Ground Station Downlink Stream To 192.168/16"

  # The placement group in which your EC2 instance is placed.
  ClusterPlacementGroup:
    Type: AWS::EC2::PlacementGroup
    Properties:
      Strategy: cluster

  ReceiverVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: `"10.0.0.0/16"`
      Tags:
        - Key: "Name"
          Value: "AWS Ground Station - PBS to dataflow endpoint Example VPC"
        - Key: "Description"
          Value: "VPC for EC2 instance receiving AWS Ground Station data"

  ReceiverSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      # Ensure your CidrBlock will always have at least one available IP address per dataflow endpoint.
      # See https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html for subent sizing guidelines.
      CidrBlock: `"10.0.0.0/24"`
      Tags:
        - Key: "Name"
          Value: "AWS Ground Station - PBS to dataflow endpoint Example Subnet"
        - Key: "Description"
          Value: "Subnet for EC2 instance receiving AWS Ground Station data"
      VpcId: !Ref ReceiverVPC

  # An ENI providing a fixed IP address for AWS Ground Station to connect to.
  ReceiverInstanceNetworkInterface:
    Type: AWS::EC2::NetworkInterface
    Properties:
      Description: Floating network interface providing a fixed IP address for AWS Ground Station to connect to.
      GroupSet:
        - !Ref InstanceSecurityGroup
      SubnetId: !Ref ReceiverSubnet

  # Attach the ENI to the EC2 instance.
  ReceiverInstanceInterfaceAttachment:
    Type: AWS::EC2::NetworkInterfaceAttachment
    Properties:
      DeleteOnTermination: false
      DeviceIndex: "1"
      InstanceId: !Ref ReceiverInstance
      NetworkInterfaceId: !Ref ReceiverInstanceNetworkInterface

```

In addition, you'll also need to create the appropriate policies and roles to allow AWS Ground Station to create an elastic network interface (ENI) in
your account.

```

  # AWS Ground Station assumes this role to create/delete ENIs in your account in order to stream data.
  DataDeliveryServiceRole:
    Type: AWS::IAM::Role
    Properties:
      Policies:
        - PolicyDocument:
            Statement:
              - Action:
                  - ec2:CreateNetworkInterface
                  - ec2:DeleteNetworkInterface
                  - ec2:CreateNetworkInterfacePermission
                  - ec2:DeleteNetworkInterfacePermission
                  - ec2:DescribeSubnets
                  - ec2:DescribeVpcs
                  - ec2:DescribeSecurityGroups
                Effect: Allow
                Resource: '*'
            Version: '2012-10-17'
          PolicyName: DataDeliveryServicePolicy
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
              - groundstation.amazonaws.com
            Action:
            - sts:AssumeRole

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

  # The instance profile for your EC2 instance.
  GeneralInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - !Ref InstanceRole

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
      Name: "SNPP JPSS Downlink DigIF Antenna Config"
      ConfigData:
        AntennaDownlinkConfig:
          SpectrumConfig:
            Bandwidth:
              Units: "MHz"
              Value: 30
            CenterFrequency:
              Units: "MHz"
              Value: 7812
            Polarization: "RIGHT_HAND"

  # The AWS Ground Station Dataflow Endpoint Config that defines the endpoint used to downlink data
  # from your satellite.
  DownlinkDigIfEndpointConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "Aqua SNPP JPSS Downlink DigIF Endpoint Config"
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
      Name: "37849 SNPP And 43013 JPSS"
      ContactPrePassDurationSeconds: 120
      ContactPostPassDurationSeconds: 60
      MinimumViableContactDurationSeconds: 180
      TrackingConfigArn: !Ref TrackingConfig
      DataflowEdges:
        - Source: !Ref SnppJpssDownlinkDigIfAntennaConfig
          Destination: !Ref DownlinkDigIfEndpointConfig

```

## Putting it together

With the above resources, you now have the ability to schedule JPSS-1 contacts for
synchronous data delivery from any of your onboarded AWS Ground Station [AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md").

The following is a complete CloudFormation template that includes all resources described
in this section combined into a single template that can be directly used in CloudFormation.

The CloudFormation template named `AquaSnppJpssTerraDigIF.yml` is designed to give you quick
access to start receiving digitized intermediate frequency (DigIF) data for the Aqua, SNPP,
JPSS-1/NOAA-20, and Terra satellites.
It contains an Amazon EC2 instance and the required CloudFormation resources to receive raw DigIF direct
broadcast data.

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
aws s3 cp s3://groundstation-cloudformation-templates-us-west-2/AquaSnppJpssTerraDigIF.yml .
```

You can view and download the template in the console by navigating to the following URL in
your browser:

```
https://s3.console.aws.amazon.com/s3/object/groundstation-cloudformation-templates-us-west-2/AquaSnppJpssTerraDigIF.yml
```

You can specify the template directly in CloudFormation using the following link:

```
https://groundstation-cloudformation-templates-us-west-2.s3.us-west-2.amazonaws.com/AquaSnppJpssTerraDigIF.yml
```

**What additional resources does the template define?**

The `AquaSnppJpssTerraDigIF` template includes the following additional resources:

- (Optional) **CloudWatch Event Triggers** - AWS Lambda
  Function that is triggered using CloudWatch Events sent by AWS Ground Station before and after a contact.
  The AWS Lambda Function will start and optionally stop your Receiver Instance.
- (Optional) **EC2 Verification for Contacts** - The option
  to use Lambda to set up a verification system of your Amazon EC2 instance(s) for contacts
  with SNS notification. It is important to note that this may incur charges depending on
  your current usage.
- **Ground Station Amazon Machine Image Retrieval Lambda**

* The option to select what software is installed in your instance and the AMI of your
  choice.
  The software options include `DDX 2.6.2 Only` and `DDX 2.6.2 with qRadio
3.6.0`. These options will continue to expand as additional software updates and
  features are released.

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

The dataflow endpoint group is set up to use the receiver instance network interface that part
of the template creates.
The receiver instance uses a dataflow endpoint application to receive the data stream from
AWS Ground Station on the port defined by the dataflow endpoint.
Once received, the data is available for consumption via UDP port 50000 on the loopback
adapter of the receiver instance.
For more information about setting up a dataflow endpoint group, see
[AWS::GroundStation::DataflowEndpointGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md").
