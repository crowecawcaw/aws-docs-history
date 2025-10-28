# Using AWS CloudTrail with interface VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and AWS CloudTrail. You can use this connection to enable
CloudTrail to communicate with your resources on your VPC without going through the
public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such the IP
address range, subnets, route tables, and network gateways. With VPC endpoints, the routing
between the VPC and AWS services is handled by the AWS network, and you can use IAM
policies to control access to service resources.

To connect your VPC to CloudTrail, you define an _interface VPC endpoint_ for
CloudTrail. An interface endpoint is an elastic network interface with a private IP address that
serves as an entry point for traffic destined to a supported AWS service. The endpoint
provides reliable, scalable connectivity to CloudTrail without requiring an internet gateway,
network address translation (NAT) instance, or VPN connection. For more information, see
[What is Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
_Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that
enables private communication between AWS services using an elastic network interface with
private IP addresses. For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/").

The following sections are for users of Amazon VPC. For more information, see [Get started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the
_Amazon VPC User Guide_.

###### Topics

- [Regions](#cloudtrail-interface-VPC-availability "#cloudtrail-interface-VPC-availability")
- [Create a VPC endpoint for CloudTrail](#create-VPC-endpoint-for-CloudTrail "#create-VPC-endpoint-for-CloudTrail")
- [Create a VPC endpoint policy for CloudTrail](#create-VPC-endpoint-policy "#create-VPC-endpoint-policy")
- [Shared subnets](#shared-subnet-cloudtrail "#shared-subnet-cloudtrail")

## Regions

AWS CloudTrail supports VPC endpoints and VPC endpoint policies in all AWS Regions in which CloudTrail is supported.

## Create a VPC endpoint for CloudTrail

To start using CloudTrail with your VPC, create an interface VPC endpoint for CloudTrail. For
more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint.html "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint.html")
in the _Amazon VPC User Guide_.

You don't need to change the settings for CloudTrail. CloudTrail calls other AWS services using
either public endpoints or private interface VPC endpoints, whichever are in use.

## Create a VPC endpoint policy for CloudTrail

A VPC endpoint policy is an IAM resource that you can attach to an interface VPC
endpoint. The default endpoint policy gives you full access to CloudTrail APIs through the
interface VPC endpoint. To control the access granted to CloudTrail from your VPC, attach a
custom endpoint policy to the interface VPC endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
- The actions that can be performed.
- The resources on which actions can be performed.

For more information about VPC endpoint policies, including how to update a policy, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md")
in the _Amazon VPC User Guide_.

Following are examples of custom VPC endpoint policies for CloudTrail.

###### Example policies:

- [Example: Allow all CloudTrail actions](#create-VPC-endpoint-policy-example1 "#create-VPC-endpoint-policy-example1")
- [Example: Allow specific CloudTrail actions](#create-VPC-endpoint-policy-example2 "#create-VPC-endpoint-policy-example2")
- [Example: Deny all CloudTrail actions](#create-VPC-endpoint-policy-example3 "#create-VPC-endpoint-policy-example3")
- [Example: Deny specific CloudTrail actions](#create-VPC-endpoint-policy-example4 "#create-VPC-endpoint-policy-example4")
- [Example: Allow all CloudTrail actions from a specific VPC](#create-VPC-endpoint-policy-example5 "#create-VPC-endpoint-policy-example5")
- [Example: Allow all CloudTrail actions from a specific VPC endpoint](#create-VPC-endpoint-policy-example6 "#create-VPC-endpoint-policy-example6")

### Example: Allow all CloudTrail actions

The following example VPC endpoint policy grants access to all CloudTrail actions for
all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "cloudtrail:*",
 "Effect": "Allow",
 "Resource": "*",
 "Principal": "*"
 }
 ]
}`

```

### Example: Allow specific CloudTrail actions

The following example VPC endpoint policy grants access to perform the `cloudtrail:ListTrails` and `cloudtrail:ListEventDataStores` actions for
all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": ["cloudtrail:ListTrails", "cloudtrail:ListEventDataStores"],
 "Effect": "Allow",
 "Principal": "*",
 "Resource": "*"
 }
 ]
}`

```

### Example: Deny all CloudTrail actions

The following example VPC endpoint policy denies access to all CloudTrail actions for
all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "cloudtrail:*",
 "Effect": "Deny",
 "Principal": "*",
 "Resource": "*"
 }
 ]
}`

```

### Example: Deny specific CloudTrail actions

The following example VPC endpoint policy denies the `cloudtrail:CreateTrail` and `cloudtrail:CreateEventDataStore` actions for
all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": ["cloudtrail:CreateTrail", "cloudtrail:CreateEventDataStore"],
 "Effect": "Deny",
 "Principal": "*",
 "Resource": "*"
 }
 ]
}`

```

### Example: Allow all CloudTrail actions from a specific VPC

The following example VPC endpoint policy grants access to perform all CloudTrail actions for
all principals on all resources but only if the requester uses the specified VPC to make the request.
Replace `vpc-id` with your VPC ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudtrail:*",
 "Resource": "*",
 "Principal": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceVpc": "`vpc-1234567890abcdef0`"
 }
 }
 }
 ]
}`

```

### Example: Allow all CloudTrail actions from a specific VPC endpoint

The following example VPC endpoint policy grants access to perform all CloudTrail actions for
all principals on all resources but only if the requester uses the specified VPC endpoint to make the request.
Replace `vpc-endpoint-id` with your VPC endpoint ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudtrail:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceVpce": "`vpce-1a2b3c4d`"
 }
 }
 }
 ]
 }`

```

## Shared subnets

A CloudTrail VPC endpoint, like any other VPC endpoint, can only be created by an owner account in the shared subnet. However, a participant account can use CloudTrail VPC endpoints in subnets that are shared with the participant account.
For more information about Amazon VPC sharing, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.
