

# Agent requirements
<a name="agent-requirements"></a>

**Note**  
This AWS Ground Station Agent guide assumes that you have onboarded to Ground Station using the [AWS Ground Station Getting started](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.html) guide.

 The AWS Ground Station Agent receiver EC2 instance requires a set of dependent AWS resources to reliably and securely deliver DigIF data to your endpoints. 

1. A VPC in which to launch the EC2 receiver.

1. An AWS KMS Key for data encryption/decryption.

1. An SSH key or EC2 Instance Profile configured for [SSM Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html).

1. Network/Security Group rules to allow the following:

   1. UDP traffic from AWS Ground Station on the ports specified in your dataflow endpoint group. The agent reserves a range of contiguous ports used to deliver data to the ingress dataflow endpoint(s).

   1. SSH access to your instance (Note: You can alternatively use AWS Session Manager to access your EC2 instance). 

   1. Read access to a publicly accessible S3 bucket for agent management.

   1. SSL traffic on port 443 allowing the agent to communicate with the AWS Ground Station service.

   1. Traffic from the AWS Ground Station managed prefix list `com.amazonaws.global.groundstation`.

 Additionally, a VPC configuration including a public subnet is required. Refer to the [ VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) for background on subnet configuration. 

Compatible configurations:

1. An Elastic IP associated with your EC2 instance in a public subnet.

1. An Elastic IP associated with an ENI in a public subnet, attached to your EC2 instance (in any subnet in the same availability zone as the public subnet).

You may use the same security group as your EC2 instance or specify one with at least the minimum set of rules consisting of:
+ UDP traffic from AWS Ground Station on the ports specified in your dataflow endpoint group.

 For example CloudFormation EC2 Data Delivery templates with these resources preconfigured, see [ Public broadcast satellite utilizing AWS Ground Station Agent (wideband) ](https://docs.aws.amazon.com/ground-station/latest/ug/examples.pbs-agent.html). 

## VPC diagrams
<a name="vpc-subnet-diagrams"></a>

**Diagram: An Elastic IP associated with your EC2 instance in a public subnet**

 ![An Elastic IP associated with your EC2 instance in a public subnet.](http://docs.aws.amazon.com/ground-station/latest/gs-agent-ug/images/digif-vpc-public-subnet.png) 

**Diagram: An Elastic IP associated with an ENI in a public subnet, attached to your EC2 instance in a private subnet**

 ![An Elastic IP associated with an ENI in a public subnet, attached to your EC2 instance in a private subnet.](http://docs.aws.amazon.com/ground-station/latest/gs-agent-ug/images/digif-vpc-private-subnet.png) 

## Supported operating system
<a name="supported-operating-system"></a>

The AWS Ground Station Agent supports the following operating systems:
+ Amazon Linux 2023 (kernel 6.12) (recommended)
+ Amazon Linux 2 (kernel 5.10)

 Supported instances types are listed in [Select Amazon EC2 instance and reserve CPU cores for your architecture](agent-instance-selection.md) 