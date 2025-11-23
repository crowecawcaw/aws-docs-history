# Amazon VPC endpoints for Amazon SWF

###### Note

AWS PrivateLink support is currently available in the AWS Top Secret - East, AWS Secret Region, and China Regions only.

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a connection
between your Amazon VPC and Amazon Simple Workflow Service workflows. You can use this connection with your Amazon SWF
workflows without crossing the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to
control your network settings, such as the IP address range, subnets, route tables, and network
gateways. For more information about VPCs, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

To connect your Amazon VPC to Amazon SWF you must first define an _interface
VPC endpoint_, which lets you connect your VPC to other AWS services. The endpoint
provides reliable, scalable connectivity, without requiring an internet gateway, network address
translation (NAT) instance, or VPN connection. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in
the _Amazon VPC User Guide_.

## Creating the Endpoint

You can create an Amazon SWF endpoint in your VPC using the AWS Management Console, the AWS Command Line Interface
(AWS CLI), an AWS SDK, the Amazon SWF API, or CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the
AWS CLI, see [Creating
an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide._

###### Note

When you create an endpoint, specify Amazon SWF as the service that you want your VPC to connect to. In the Amazon VPC console, service names vary based on the AWS
Region. For example, in the AWS Top Secret - East Region, the service name for Amazon SWF is **com.amazonaws.us-iso-east-1.swf**.

For information about creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource
in the _CloudFormation User Guide_.

## Amazon VPC Endpoint Policies

To control connectivity access to Amazon SWF you can attach an AWS Identity and Access Management (IAM) endpoint
policy while creating an Amazon VPC endpoint. You can create complex IAM rules by attaching
multiple endpoint policies. For more information, see:

- [Amazon Virtual Private Cloud Endpoint Policies for Amazon SWF](swf-vpc-iam.md "swf-vpc-iam.md")
- [Controlling Access to Services with
  VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md")
