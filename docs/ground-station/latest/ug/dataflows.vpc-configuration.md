

# Set up and configure Amazon VPC
<a name="dataflows.vpc-configuration"></a>

A full guide to set up a VPC is beyond the scope of this guide. For an in-depth understanding please refer to the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). 

In this section, it is described how your Amazon EC2 and dataflow endpoint may exist within a VPC. AWS Ground Station does not support multiple delivery points for a given dataflow - it is expected that each dataflow terminates to a single EC2 receiver. As we expect a single EC2 receiver, the configuration is not multi-AZ redundant. For full examples which will use your VPC, please see [Example mission profile configurations](examples.md). 

## VPC Configuration with AWS Ground Station Agent
<a name="dataflows.vpc-configuration.agent"></a>

 ![AWS Ground Station architecture with VPC, private and public subnets, and Amazon EC2 instance.](http://docs.aws.amazon.com/ground-station/latest/ug/images/dataflows.vpc-gs-agent.png) 

Your satellite data is provided to an AWS Ground Station Agent instance that is proximate to the antenna. The AWS Ground Station Agent will stripe and then encrypt your data using the AWS KMS key you provide. Each stripe is sent to your [ Amazon EC2 Elastic IP (EIP) ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) from the source antenna across the AWS Network backbone. The data arrives at your EC2 instance via the [Amazon EC2 Elastic Network Interface (ENI) ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) attached. Once on your EC2 instance, the installed AWS Ground Station Agent will decrypt your data and perform forward error correction (FEC) to recover any dropped data, then forward it to the IP and port you specified in your setup. 

The below list calls out unique setup considerations when setting up your VPC for AWS Ground Station Agent delivery. 

 **Security Group** - It is recommended you set up a security group dedicated to only AWS Ground Station traffic. This security group should allow UDP ingress traffic on the same port range you specify in your Dataflow Endpoint Group. AWS Ground Station maintains an AWS-managed prefix list to restrict your permissions to only AWS Ground Station IP addresses. See [AWS Managed Prefix Lists ](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) for details on how to replace the *PrefixListId* for your deployment regions. 

 **Elastic Network Interface (ENI)** - You will need to associate the above security group with this ENI and place it in your public subnet. 

**Note**  
 The default quota for number of security groups attached per ENI is 5. This is an adjustable limit up to 16, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-security-groups). 

 The following CloudFormation template demonstrates how to create the infrastructure described in this section. 

```
{{ReceiveInstanceEIP}}:
  Type: AWS::EC2::EIP
  Properties:
    Domain: 'vpc'

{{InstanceSecurityGroup}}:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: {{AWS Ground Station receiver instance security group.}}
    VpcId:{{YourVpcId}}
    SecurityGroupIngress:
      # Add additional items here.
      - IpProtocol: udp
        FromPort: {{your-port-start-range}}
        ToPort: {{your-port-end-range}}
        PrefixListIds:
          - PrefixListId: {{com.amazonaws.global.groundstation}}
        Description: {{"Allow AWS Ground Station Downlink ingress."}}

{{InstanceNetworkInterface}}:
  Type: AWS::EC2::NetworkInterface
  Properties:
    Description: {{ENI for AWS Ground Station to connect to.}}
    GroupSet:
      - !Ref {{InstanceSecurityGroup}}
    SubnetId: {{A Public Subnet}}

{{ReceiveInstanceEIPAllocation}}:
  Type: AWS::EC2::EIPAssociation
  Properties:
    AllocationId:
      Fn::GetAtt: [ {{ReceiveInstanceEIP}}, AllocationId ]
    NetworkInterfaceId:
      Ref: {{InstanceNetworkInterface}}
```

## VPC configuration with a dataflow endpoint
<a name="dataflows.vpc-configuration.dataflow-endpoint"></a>

 ![Diagram showing two VPCs with Amazon EC2 instances running endpoint applications.](http://docs.aws.amazon.com/ground-station/latest/ug/images/dataflows.vpc-dataflow-endpoint-application.png) 

Your satellite data is provided to a dataflow endpoint application instance that is proximate to the antenna. The data is then sent through cross-account [Amazon EC2 Elastic Network Interface (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) from a VPC owned by AWS Ground Station. The data then arrives at your EC2 instance via the ENI attached to your Amazon EC2 instance. The installed dataflow endpoint application will then forward it to the IP and port you specified in your setup. The reverse of this flow occurs for uplink connections. 

 The below list calls out unique setup considerations when setting up your VPC for dataflow endpoint delivery. 

**Note**  
 The default quota for number of security groups attached per ENI is 5. This is an adjustable limit up to 16, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-security-groups). 

 **IAM Role** - The IAM Role is part of the Dataflow Endpoint and is not shown in the diagram. The IAM role that is used to create and attach the cross-account ENI to the AWS Ground Station Amazon EC2 instance. 

 **Security Group 1** - This security group is attached to the ENI which will be associated to the Amazon EC2 instance in your account. It needs to allow UDP traffic from Security Group 2 on the ports specified in your *dataflow-endpoint-group*. 

 **Elastic Network Interface (ENI) 1** - You will need to associate Security Group 1 with this ENI and place it in a subnet. 

 **Subnet** - You will need to ensure that there is at least one available IP address per dataflow for the Amazon EC2 instance in your account. For more details on subnet sizing see, [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) 

 **Security Group 2** - This security group is referenced in the Dataflow Endpoint. This security group will be attached to the ENI that AWS Ground Station will use to place data into your account. 

 **Region** - For more information on the supported regions for cross-region connections, see [Use cross-region data delivery](dataflows.cross-region-data-delivery.md). 

 The following CloudFormation template demonstrates how to create the infrastructure described in this section. 

```
{{DataflowEndpointSecurityGroup}}:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Security Group for AWS Ground Station registration of Dataflow Endpoint Groups
    VpcId: {{YourVpcId}}
  
{{AWSGroundStationSecurityGroupEgress}}:
  Type: AWS::EC2::SecurityGroupEgress
  Properties:
    GroupId: !Ref: {{DataflowEndpointSecurityGroup}}
    IpProtocol: udp
    FromPort: {{55555}}
    ToPort: {{55555}}
    CidrIp: {{10.0.0.0/8}}
    Description: {{"Allow AWS Ground Station to send UDP traffic on port 55555 to the 10/8 range."}}

{{InstanceSecurityGroup}}:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: {{AWS Ground Station receiver instance security group.}}
    VpcId: {{YourVpcId}}
    SecurityGroupIngress:
      - IpProtocol: udp
        FromPort: {{55555}}
        ToPort: {{55555}}
        SourceSecurityGroupId: {{!Ref DataflowEndpointSecurityGroup}}
        Description: {{"Allow AWS Ground Station Ingress from DataflowEndpointSecurityGroup"}}

{{ReceiverSubnet}}:
  Type: AWS::EC2::Subnet
  Properties:
    # Ensure your CidrBlock will always have at least one available IP address per dataflow endpoint.
    # See https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html for subent sizing guidelines.
    CidrBlock: {{"10.0.0.0/24"}}
    Tags:
      - Key: "Name"
        Value: {{"AWS Ground Station - Dataflow endpoint Example Subnet"}}
      - Key: "Description"
        Value: {{"Subnet for EC2 instance receiving AWS Ground Station data"}}
    VpcId: !Ref ReceiverVPC
```