# AWS PrivateLink for AWS Account Management

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can access the AWS Account Management
service from within the VPC without having to cross the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to
control your network settings, such as the IP address range, subnets, route tables, and
network gateways. For more information about VPCs, see the _[Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")_.

To connect your Amazon VPC to Account Management, you must first define an _interface VPC endpoint_, which lets you connect your VPC to other AWS
services. The endpoint provides reliable, scalable connectivity, without requiring an
internet gateway, network address translation (NAT) instance, or VPN connection. For more
information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

## Creating the Endpoint

You can create an AWS Account Management endpoint in your VPC using the AWS Management Console, the AWS Command Line Interface
(AWS CLI), an AWS SDK, the AWS Account Management API, or AWS CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or
the AWS CLI, see [Creating an Interface
Endpoint](../../../vpc/latest/userguide/create-endpoint-service.md "../../../vpc/latest/userguide/create-endpoint-service.md") in the _Amazon VPC User Guide._

###### Note

When you create an endpoint, specify Account Management as the service that you want your VPC
to connect to, using the following format:

```
com.amazonaws.us-east-1.account
```

You must use the string exactly as shown, specifying the `us-east-1` Region. As a global service, Account Management is
hosted in only that one AWS Region.

For information about creating and configuring an endpoint using AWS CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md")
resource in the _AWS CloudFormation User Guide_.

## Amazon VPC Endpoint Policies

You can control what actions can performed through this service endpoint by attaching
an endpoint policy when you create the Amazon VPC endpoint. You can create complex IAM
rules by attaching multiple endpoint policies. For more information, see:

- [Amazon Virtual Private Cloud endpoint policies for Account Management](vpc-iam.md "vpc-iam.md")
- [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.
