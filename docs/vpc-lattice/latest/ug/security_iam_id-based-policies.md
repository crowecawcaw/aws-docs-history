# Identity-based policies for

Amazon VPC Lattice

By default, users and roles don't have permission to create or modify VPC Lattice
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by VPC Lattice, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon VPC Lattice](../../../service-authorization/latest/reference/list_amazonvpclattice.md "../../../service-authorization/latest/reference/list_amazonvpclattice.md") in the _Service Authorization Reference_.

###### Contents

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Additional
  required permissions for full access](#security_iam_id-based-policy-additional-permissions "#security_iam_id-based-policy-additional-permissions")
- [Identity-based policy examples
  for VPC Lattice](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete VPC Lattice resources in your
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
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
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

## Additional

required permissions for full access

To use other AWS services that VPC Lattice is integrated with and the entire suite of
VPC Lattice features, you must have specific additional permissions. These permissions are
not included in the `VPCLatticeFullAccess` managed policy because of the
[confused
deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") privilege escalation risk.

You must attach the following policy to your role and use it along with the
`VPCLatticeFullAccess` managed policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "firehose:TagDeliveryStream",
 "lambda:AddPermission",
 "s3:PutBucketPolicy"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutResourcePolicy"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "vpc-lattice.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:PutRolePolicy"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/vpc-lattice.amazonaws.com/AWSServiceRoleForVpcLattice"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:PutRolePolicy"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery*"
 }
 ]
}`

```

This policy provides the following additional permissions:

- `iam:AttachRolePolicy`: Allows you to attach the specified managed
  policy to the specified IAM role.
- `iam:PutRolePolicy`: Allows you to add or update an inline policy
  document that is embedded in the specified IAM role.
- `s3:PutBucketPolicy`: Allows you to apply a bucket policy to an Amazon S3
  bucket.
- `firehose:TagDeliveryStream`: Allows you to add or update tags for
  Firehose delivery streams.

## Identity-based policy examples

for VPC Lattice

###### Topics

- [Example policy: Manage VPC associations to a service network](#security_iam_id-based-policy-examples-vpc-to-service-network-association "#security_iam_id-based-policy-examples-vpc-to-service-network-association")
- [Example policy: Create service associations to a service network](#security_iam_id-based-policy-examples-service-to-service-network-association "#security_iam_id-based-policy-examples-service-to-service-network-association")
- [Example policy: Add tags to resources](#security_iam_id-based-policy-examples-tag-resources "#security_iam_id-based-policy-examples-tag-resources")
- [Example policy: Create a service-linked role](#security_iam_id-based-policy-examples-service-linked-role "#security_iam_id-based-policy-examples-service-linked-role")

### Example policy: Manage VPC associations to a service network

The following example demonstrates a policy that gives users with this policy the
permission to create, update, and delete the VPC associations to a service network,
but only for the VPC and service network specified in the condition. For more
information about specifying condition keys, see [Policy
condition keys for VPC Lattice](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "vpc-lattice:CreateServiceNetworkVpcAssociation",
 "vpc-lattice:UpdateServiceNetworkVpcAssociation",
 "vpc-lattice:DeleteServiceNetworkVpcAssociation"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "vpc-lattice:ServiceNetworkArn": "arn:aws:vpc-lattice:us-west-2:`123456789012`:servicenetwork/sn-`903004f88example`",
 "vpc-lattice:VpcId": "vpc-`1a2b3c4d`"
 }
 }
 }
 ]
}`

```

### Example policy: Create service associations to a service network

If you are not using condition keys to control access to VPC Lattice resources, you
can specify the ARNs of resources in the `Resource` element to control
access instead.

The following example demonstrates a policy that limits the service associations
to a service network that users with this policy can create by specifying the ARNs of
the service and service network that can be used with the
`CreateServiceNetworkServiceAssociation` API action. For more
information about specifying the ARN values, see [Policy
resources for VPC Lattice](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "vpc-lattice:CreateServiceNetworkServiceAssociation"
 ],
 "Resource": [
 "arn:aws:vpc-lattice:us-west-2:`123456789012`:servicenetworkserviceassociation/*",
 "arn:aws:vpc-lattice:us-west-2:`123456789012`:service/svc-`04d5cc9b88example`",
 "arn:aws:vpc-lattice:us-west-2:`123456789012`:servicenetwork/sn-`903004f88example`"
 ]
 }
 ]
}`

```

### Example policy: Add tags to resources

The following example demonstrates a policy that gives users with this policy
permission to create tags on VPC Lattice resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "vpc-lattice:TagResource"
 ],
 "Resource": "arn:aws:vpc-lattice:us-west-2:`123456789012`:*/*"
 }
 ]
}`

```

### Example policy: Create a service-linked role

VPC Lattice requires permissions to create a service-linked role the first time that
any user in your AWS account creates VPC Lattice resources. If the service-linked
role does not exist already, VPC Lattice creates it in your account. The service-linked
role gives permissions to VPC Lattice so that it can call other AWS services on your
behalf. For more information, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md "using-service-linked-roles.md").

For automatic role creation to succeed, users must have permissions for the
`iam:CreateServiceLinkedRole` action.

```
"Action": "iam:CreateServiceLinkedRole"
```

The following example demonstrates a policy that gives users with this policy
permission to create a service-linked role for VPC Lattice.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/vpc-lattice.amazonaws.com/AWSServiceRoleForVpcLattice",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName":"vpc-lattice.amazonaws.com"
 }
 }
 }
 ]
}`

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.
