# Creating Amazon VPC endpoints for Step Functions

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a connection
between your Amazon VPC and AWS Step Functions workflows. You can use this connection with your Step Functions
workflows without crossing the public internet. Amazon VPC endpoints are supported by Standard Workflows,
Express Workflows, and Synchronous Express Workflows.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to
control your network settings, such as the IP address range, subnets, route tables, and network
gateways. For more information about VPCs, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

To connect your Amazon VPC to Step Functions, you must first define an _interface
VPC endpoint_, which lets you connect your VPC to other AWS services. The endpoint
provides reliable, scalable connectivity, without requiring an internet gateway, network address
translation (NAT) instance, or VPN connection. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in
the _Amazon VPC User Guide_.

## Creating the Endpoint

You can create an AWS Step Functions endpoint in your VPC using the AWS Management Console, the AWS Command Line Interface
(AWS CLI), an AWS SDK, the AWS Step Functions API, or AWS CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the
AWS CLI, see [Creating
an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide._

###### Note

When you create an endpoint, specify Step Functions as the service that you want your VPC to
connect to. In the Amazon VPC console, service names vary based on the AWS Region. For example,
if you choose US East (N. Virginia), the service name for Standard Workflows and Express Workflows is
**com.amazonaws.us-east-1.states**, and the service name for Synchronous Express Workflows is
**com.amazonaws.us-east-1.sync-states**.

###### Note

It's possible to use VPC Endpoints without overriding the endpoint in the SDK
through [Private DNS](../../../vpc/latest/privatelink/verify-domains.md "../../../vpc/latest/privatelink/verify-domains.md").
However, if you want to override the endpoint in the SDK for Synchronous Express Workflows,
you need to set `DisableHostPrefixInjection` configuration to `true`. Example (Java SDK V2):

```
SfnClient.builder()
  .endpointOverride(URI.create("https://vpce-{vpceId}.sync-states.us-east-1.vpce.amazonaws.com"))
  .overrideConfiguration(ClientOverrideConfiguration.builder()
    .advancedOptions(ImmutableMap.of(SdkAdvancedClientOption.DISABLE_HOST_PREFIX_INJECTION, true))
    .build())
  .build();
```

For information about creating and configuring an endpoint using AWS CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource
in the _AWS CloudFormation User Guide_.

## Amazon VPC Endpoint Policies

To control connectivity access to Step Functions you can attach an AWS Identity and Access Management (IAM) endpoint
policy while creating an Amazon VPC endpoint. You can create complex IAM rules by attaching
multiple endpoint policies. For more information, see:

- [Amazon Virtual Private Cloud Endpoint Policies for Step Functions](#vpc-iam "#vpc-iam")
- [Creating granular permissions for non-admin users in Step Functions](concept-create-iam-advanced.md "concept-create-iam-advanced.md")
- [Controlling Access to Services with
  VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md")

## Amazon Virtual Private Cloud Endpoint Policies for Step Functions

You can create an Amazon VPC endpoint policy for Step Functions in which you specify the
following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which the actions can be performed.

The following example shows an Amazon VPC endpoint policy that allows one user to create
state machines, and denies all other users permission to delete state machines. The example
policy also grants all users execution permission.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "states:ListExecutions", "states:StartExecution", "states:StopExecution", "states:DescribeExecution"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Principal": "*"
 },
 {
 "Action": "states:CreateStateMachine",
 "Resource": "*",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/MyUser"
 }
 },
 {
 "Action": "states:DeleteStateMachine",
 "Resource": "*",
 "Effect": "Deny",
 "Principal": "*"
 }
 ]
}`

```

For more information about creating endpoint policies, see the following:

- [Creating granular permissions for non-admin users in Step Functions](concept-create-iam-advanced.md "concept-create-iam-advanced.md")
- [Controlling Access to Services with
  VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md")
