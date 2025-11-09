# AWS managed policies for MemoryDB

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: MemoryDBServiceRolePolicy

You cannot attach the MemoryDBServiceRolePolicy AWS managed policy to identities in your account. This policy is part of the AWS MemoryDB service-linked role.
This role allows the service to manage network interfaces and security groups in your account.

MemoryDB uses the permissions in this policy to manage EC2 security groups and network interfaces. This is required to manage MemoryDB clusters.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "AmazonMemoryDBManaged"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws-cn:ec2:*:*:network-interface/*",
 "arn:aws-cn:ec2:*:*:subnet/*",
 "arn:aws-cn:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/AmazonMemoryDBManaged": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "arn:aws-cn:ec2:*:*:security-group/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/MemoryDB"
 }
 }
 }
 ]
}`

```

## AWS-managed (predefined) policies

for MemoryDB

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. Managed policies grant necessary permissions for
common use cases so you can avoid having to investigate what permissions are needed.
For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account,
are specific to MemoryDB:

### AmazonMemoryDBReadOnlyAccess

You can attach the `AmazonMemoryDBReadOnlyAccess` policy to your IAM identities. This policy grants administrative permissions that allow read-only access to all MemoryDB resources.

**AmazonMemoryDBReadOnlyAccess** - Grants
read-only access to MemoryDB resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "memorydb:Describe*",
 "memorydb:List*"
 ],
 "Resource": "*"
 }]
}`

```

### AmazonMemoryDBFullAccess

You can attach the `AmazonMemoryDBFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to all MemoryDB resources.

**AmazonMemoryDBFullAccess** - Grants full
access to MemoryDB resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "memorydb:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/memorydb.amazonaws.com/AWSServiceRoleForMemoryDB",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "memorydb.amazonaws.com"
 }
 }
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "memorydb:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws-cn:iam::*:role/aws-service-role/memorydb.amazonaws.com/AWSServiceRoleForMemoryDB",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "memorydb.amazonaws.com"
 }
 }
 }
 ]
}`

```

You can also create your own custom IAM policies to allow permissions for
MemoryDB API actions. You can attach these custom policies to the IAM users or
groups that require those permissions.

## MemoryDB updates to AWS managed

policies

View details about updates to AWS managed policies for MemoryDB since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the MemoryDB Document history page.

| Change                                                                                                                                                                 | Description                                                                                                                                                                                                            | Date       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [AWS managed policy: MemoryDBServiceRolePolicy](#security-iam-awsmanpol-memorydbServiceRolePolicy "#security-iam-awsmanpol-memorydbServiceRolePolicy") – Adding policy | MemoryDBServiceRolePolicy added the permission for memorydb:ReplicateMultiRegionClusterData. This permission will allow the service-linked role to replicate data for MemoryDB multi-Region clusters.                  | 12/01/2024 |
| [AmazonMemoryDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Adding policy        | MemoryDB added new permissions to describe and list supported resources.<br>These permissions are required for MemoryDB to query all of the supported resources in an account.                                         | 10/07/2021 |
| [AmazonMemoryDBReadOnlyAccess](#iam.identitybasedpolicies.predefinedpolicies-readonly "#iam.identitybasedpolicies.predefinedpolicies-readonly") – Adding policy        | MemoryDB added new permissions to describe and list supported resources.<br>These permissions are required for MemoryDB to create account-based applications by querying all of the supported resources in an account. | 10/07/2021 |
| MemoryDB started tracking changes                                                                                                                                      | Service launch                                                                                                                                                                                                         | 8/19/2021  |
