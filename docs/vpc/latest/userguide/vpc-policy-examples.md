# Amazon VPC policy examples

By default, IAM roles don't have permission to create or modify VPC resources. They
also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM
administrator must create IAM policies that grant roles permission to perform specific
API operations on the specified resources they need. The administrator must then attach
those policies to the IAM roles that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_.

###### Contents

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Use the Amazon VPC console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Create a VPC with a public
  subnet](#vpc-public-subnet-iam "#vpc-public-subnet-iam")
- [Modify and delete VPC resources](#modify-vpc-resources-iam "#modify-vpc-resources-iam")
- [Manage security groups](#vpc-security-groups-iam "#vpc-security-groups-iam")
- [Manage security group rules](#vpc-security-group-rules-iam "#vpc-security-group-rules-iam")
- [Launch instances into a specific subnet](#subnet-sg-example-iam "#subnet-sg-example-iam")
- [Launch instances into a specific VPC](#subnet-ami-example-iam "#subnet-ami-example-iam")
- [Block public access to VPCs and subnets](#vpc-bpa-example-iam "#vpc-bpa-example-iam")
- [Additional Amazon VPC policy examples](#security-iam-additional-examples "#security-iam-additional-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon VPC resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Use the Amazon VPC console

To access the Amazon VPC console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the Amazon VPC resources in
your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (IAM roles) with that policy.

The following policy grants a role permission to list resources in the VPC
console, but not to create, update, or delete them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAddresses",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeClassicLinkInstances",
 "ec2:DescribeClientVpnEndpoints",
 "ec2:DescribeCustomerGateways",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeEgressOnlyInternetGateways",
 "ec2:DescribeFlowLogs",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeManagedPrefixLists",
 "ec2:DescribeMovingAddresses",
 "ec2:DescribeNatGateways",
 "ec2:DescribeNetworkAcls",
 "ec2:DescribeNetworkInterfaceAttribute",
 "ec2:DescribeNetworkInterfacePermissions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribePrefixLists",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroupReferences",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeStaleSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeTags",
 "ec2:DescribeTrafficMirrorFilters",
 "ec2:DescribeTrafficMirrorSessions",
 "ec2:DescribeTrafficMirrorTargets",
 "ec2:DescribeTransitGateways",
 "ec2:DescribeTransitGatewayVpcAttachments",
 "ec2:DescribeTransitGatewayRouteTables",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcClassicLink",
 "ec2:DescribeVpcClassicLinkDnsSupport",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcEndpointConnectionNotifications",
 "ec2:DescribeVpcEndpointConnections",
 "ec2:DescribeVpcEndpointServiceConfigurations",
 "ec2:DescribeVpcEndpointServicePermissions",
 "ec2:DescribeVpcEndpointServices",
 "ec2:DescribeVpcPeeringConnections",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpnConnections",
 "ec2:DescribeVpnGateways",
 "ec2:GetManagedPrefixListAssociations",
 "ec2:GetManagedPrefixListEntries"
 ],
 "Resource": "*"
 }
 ]
}`

```

You don't need to allow minimum console permissions for roles that are making
calls only to the AWS CLI or the AWS API. Instead, allow access only to actions that
match the API operation that the role needs to perform.

## Create a VPC with a public

subnet

The following example enables roles to create VPCs, subnets, route tables, and
internet gateways. Roles can also attach an internet gateway to a VPC and create
routes in route tables. The `ec2:ModifyVpcAttribute` action enables roles
to enable DNS hostnames for the VPC, so that each instance launched into a VPC
receives a DNS hostname.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpc",
 "ec2:CreateSubnet",
 "ec2:DescribeAvailabilityZones",
 "ec2:CreateRouteTable",
 "ec2:CreateRoute",
 "ec2:CreateInternetGateway",
 "ec2:AttachInternetGateway",
 "ec2:AssociateRouteTable",
 "ec2:ModifyVpcAttribute"
 ],
 "Resource": "*"
 }
 ]
}`

```

The preceding policy also enables roles to create a VPC in the Amazon VPC
console.

## Modify and delete VPC resources

You might want to control the VPC resources that roles can modify or delete. For
example, the following policy allows roles to work with and delete route tables that
have the tag `Purpose=Test`. The policy also specifies that roles can
only delete internet gateways that have the tag `Purpose=Test`. Roles
cannot work with route tables or internet gateways that do not have this tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DeleteInternetGateway",
 "Resource": "arn:aws:ec2:*:*:internet-gateway/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/`Purpose`": "`Test`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteRouteTable",
 "ec2:CreateRoute",
 "ec2:ReplaceRoute",
 "ec2:DeleteRoute"
 ],
 "Resource": "arn:aws:ec2:*:*:route-table/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/`Purpose`": "`Test`"
 }
 }
 }
 ]
}`

```

## Manage security groups

The following policy allows roles to manage security groups. The first statement
allows roles to delete any security group with the tag `Stack=test` and
to manage the inbound and outbound rules for any security group with the tag
`Stack=test`. The second statement requires roles to tag any security
groups that they create with the tag `Stack=Test`. The third statement
allows roles to create tags when creating a security group. The fourth statement
allows roles to view any security group and security group rule. The fifth statement
allows roles to create a security group in a VPC.

###### Note

This policy cannot be used by the AWS CloudFormation service to create a security group with required tags. If you remove the condition on the `ec2:CreateSecurityGroup` action that requires the tag, the policy will work.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RevokeSecurityGroupIngress",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:DeleteSecurityGroup",
 "ec2:ModifySecurityGroupRules",
 "ec2:UpdateSecurityGroupRuleDescriptionsIngress"
 ],
 "Resource": "arn:aws:ec2:*:*:security-group/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/Stack": "test"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSecurityGroup",
 "Resource": "arn:aws:ec2:*:*:security-group/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Stack": "test"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "Stack"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:*:*:security-group/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateSecurityGroup"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeVpcs",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSecurityGroup",
 "Resource": "arn:aws:ec2:*:*:vpc/*"
 }
 ]
}`

```

To allow roles to change the security group that's associated with an instance,
add the `ec2:ModifyInstanceAttribute` action to your policy.

To allow roles to change security groups for a network interface, add the
`ec2:ModifyNetworkInterfaceAttribute` action to your policy.

## Manage security group rules

The following policy grants roles permission to view all security groups and
security group rules, add and remove inbound and outbound rules for the security
groups for a specific VPC, and modify rule descriptions for the specified VPC. The
first statement uses the `ec2:Vpc` condition key to scope permissions to
a specific VPC.

The second statement grants roles permission to describe all security groups,
security group rules, and tags. This enables roles to view security group rules in
order to modify them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
 "ec2:ModifySecurityGroupRules"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:security-group/*",
 "Condition": {
 "ArnEquals": {
 "ec2:Vpc": "arn:aws:ec2:`us-east-1`:`123456789012`:vpc/`vpc-1234567890abcdef0`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeTags"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifySecurityGroupRules"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:security-group-rule/*"
 }
 ]
}`

```

## Launch instances into a specific subnet

The following policy grants roles permission to launch instances into a specific
subnet and to use a specific security group in the request. The policy does this by
specifying the ARN for the subnet and the ARN for the security group. If roles
attempt to launch an instance into a different subnet or using a different security
group, the request will fail (unless another policy or statement grants roles
permission to do so).

The policy also grants permission to use the network interface resource. When
launching into a subnet, the `RunInstances` request creates a primary
network interface by default, so the role needs permission to create this resource
when launching the instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`::image/ami-*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:instance/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:subnet/`subnet-1234567890abcdef0`",
 "arn:aws:ec2:`us-east-1`:`123456789012`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:volume/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:security-group/`sg-0abcdef1234567890`"
 ]
 }
 ]
}`

```

## Launch instances into a specific VPC

The following policy grants roles permission to launch instances into any subnet
within a specific VPC. The policy does this by applying a condition key
(`ec2:Vpc`) to the subnet resource.

The policy also grants roles permission to launch instances using only AMIs that
have the tag "`department=dev`".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:subnet/*",
 "Condition": {
 "ArnEquals": {
 "ec2:Vpc": "arn:aws:ec2:`us-east-1`:`123456789012`:vpc/`vpc-1234567890abcdef0`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "arn:aws:ec2:`us-east-1`::image/ami-*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/`department`": "`dev`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`123456789012`:instance/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:volume/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:key-pair/*",
 "arn:aws:ec2:`us-east-1`:`123456789012`:security-group/*"
 ]
 }
 ]
}`

```

## Block public access to VPCs and subnets

The following policy examples grant roles permission to work with the [VPC Block Public Access (BPA) feature](security-vpc-bpa.md "security-vpc-bpa.md") to block public access to resources in VPCs and subnets.

Example 1 - Allow read-only access to VPC BPA account-wide settings and VPC BPA exclusions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VPCBPAReadOnlyAccess",
 "Action": [
 "ec2:DescribeVpcBlockPublicAccessOptions",
 "ec2:DescribeVpcBlockPublicAccessExclusions"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Example 2 - Allow full read and write access to VPC BPA account-wide settings and VPC BPA exclusions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VPCBPAFullAccess",
 "Action": [
 "ec2:DescribeVpcBlockPublicAccessOptions",
 "ec2:DescribeVpcBlockPublicAccessExclusions",
 "ec2:ModifyVpcBlockPublicAccessOptions",
 "ec2:CreateVpcBlockPublicAccessExclusion",
 "ec2:ModifyVpcBlockPublicAccessExclusion",
 "ec2:DeleteVpcBlockPublicAccessExclusion"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Example 3 - Allow access to all EC2 APIs except modifying VPC BPA settings and creating exclusions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2FullAccess",
 "Action": [
 "ec2:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "VPCBPAPartialAccess",
 "Action": [
 "ec2:ModifyVpcBlockPublicAccessOptions",
 "ec2:CreateVpcBlockPublicAccessExclusion"
 ],
 "Effect": "Deny",
 "Resource": "*"
 }
 ]
}`

```

## Additional Amazon VPC policy examples

You can find additional example IAM policies related to Amazon VPC in the following documentation:

- [Managed prefix lists](managed-prefix-lists.md#managed-prefix-lists-iam "managed-prefix-lists.md#managed-prefix-lists-iam")
- [Traffic mirroring](../mirroring/traffic-mirroring-security.md "../mirroring/traffic-mirroring-security.md")
- [Transit gateways](../tgw/transit-gateway-authentication-access-control.md#tgw-example-iam-policies "../tgw/transit-gateway-authentication-access-control.md#tgw-example-iam-policies")
- [VPC endpoints and VPC endpoint services (AWS PrivateLink)](../privatelink/security_iam_id-based-policy-examples.md "../privatelink/security_iam_id-based-policy-examples.md")
- [VPC peering](../peering/security-iam.md "../peering/security-iam.md")
