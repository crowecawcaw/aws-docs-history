# Using identity-based policies (IAM

policies) for AWS Control Tower

This topic provides examples of identity-based policies that demonstrate how an account
administrator can attach permissions policies to IAM identities (that is, users, groups,
and roles) and thereby grant permissions to perform operations on AWS Control Tower resources.

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available for you to manage access to your AWS Control Tower resources. For
more information, see [Overview of managing access permissions to
your AWS Control Tower resources](access-control-overview.md "access-control-overview.md").

## AWSControlTowerAdmin role

This role provides AWS Control Tower with access to infrastructure critical to maintaining the
landing zone. The `AWSControlTowerAdmin` role requires an attached managed
policy and a role trust policy for the IAM role. A _role trust
policy_ is a resource-based policy, specifying which principals can assume
the role.

Here's an example snippet for this role trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "controltower.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

To create this role from the AWS CLI, and put it into a file called
`trust.json`, here's an example CLI command:

```
aws iam create-role --role-name AWSControlTowerAdmin --path /service-role/ --assume-role-policy-document file://trust.json
```

This role requires two IAM policies.

1. An inline policy, for example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeAvailabilityZones",
 "Resource": "*"
 }
 ]
}`

```

2. The managed policy that follows, which is the
   `AWSControlTowerServiceRolePolicy`.

## AWSControlTowerServiceRolePolicy

The **AWSControlTowerServiceRolePolicy** is an AWS-managed policy
that defines permissions to create and manage AWS Control Tower resources, such as AWS
CloudFormation stacksets and stack instances, AWS CloudTrail log files, a configuration aggregator
for AWS Control Tower, as well as AWS Organizations accounts and organizational units (OUs) that are
governed by AWS Control Tower.

Updates to this managed policy are summarized in the table, [Managed policies for AWS Control Tower](managed-policies-table.md "managed-policies-table.md").

For more information, see [AWSControlTowerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSControlTowerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSControlTowerServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

Role trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "controltower.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The inline policy is `AWSControlTowerAdminPolicy`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ec2:DescribeAvailabilityZones",
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

## AWSControlTowerIdentityCenterManagementPolicy

This policy provides permissions to configure the IAM Identity Center (IdC) resources in the member accounts enrolled with AWS Control Tower. When you select IAM Identity Center as your identity provider during landing zone setup (or update) in AWS Control Tower, this policy is attached to the `AWSControlTowerAdmin` role.

To view more details about the policy, including the latest version of the JSON policy document, see [AWSControlTowerIdentityCenterManagementPolicy](../../../aws-managed-policy/latest/reference/AWSControlTowerIdentityCenterManagementPolicy.md "../../../aws-managed-policy/latest/reference/AWSControlTowerIdentityCenterManagementPolicy.md") in the _AWS Managed Policy Reference Guide_.

## AWSControlTowerStackSetRole

CloudFormation assumes this role to deploy stack sets in accounts created by AWS Control Tower. Inline
Policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWSControlTowerExecution"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

**Trust policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## AWSControlTowerCloudTrailRolePolicy

AWS Control Tower enables CloudTrail as a best practice and provides this role to CloudTrail. CloudTrail assumes
this role to create and publish CloudTrail logs.

**Managed Policy:** `AWSControlTowerCloudTrailRolePolicy`

This role uses the AWS-managed policy `AWSControlTowerCloudTrailRolePolicy`,
which grants CloudTrail the permissions necessary to publish audit logs to Amazon CloudWatch Logs on behalf of
AWS Control Tower. This managed policy replaces the inline policy that was previously used for this role,
enabling AWS to update the policy without customer intervention.

For more information, see [AWSControlTowerCloudTrailRolePolicy](../../../aws-managed-policy/latest/reference/AWSControlTowerCloudTrailRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSControlTowerCloudTrailRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

Updates to this managed policy are summarized in the table, [Managed policies for AWS Control Tower](managed-policies-table.md "managed-policies-table.md").

###### Note

Prior to the introduction of the managed policy, this role used an inline policy with
equivalent permissions. The inline policy has been replaced by the managed policy to
enable seamless updates.

**Previous Inline Policy (for reference):**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "logs:CreateLogStream",
 "Resource": "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs:*",
 "Effect": "Allow"
 },
 {
 "Action": "logs:PutLogEvents",
 "Resource": "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs:*",
 "Effect": "Allow"
 }
 ]
}`

```

**Trust policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## AWSControlTowerBlueprintAccess role

requirements

AWS Control Tower requires you to create the `AWSControlTowerBlueprintAccess` role
in the designated blueprint hub account, within the same organization.

**Role name**

The role name must be `AWSControlTowerBlueprintAccess`.

**Role trust policy**

The role must be set up to trust the following principals:

- The principal that uses AWS Control Tower in the management account.
- The `AWSControlTowerAdmin` role in the management account.

The following example shows a least-privilege trust policy. When you make your own
policy, replace the term `YourManagementAccountId` with the
actual acccount ID of your AWS Control Tower management account, and replace the term
`YourControlTowerUserRole` with the identifier of the IAM
role for your management account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/service-role/AWSControlTowerAdmin",
 "arn:aws:iam::`111122223333`:role/`YourControlTowerUserRole`"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

**Role permissions**

You are required to attach the managed policy
**AWSServiceCatalogAdminFullAccess** to the role.

## AWSServiceRoleForAWSControlTower

This role provides AWS Control Tower with access to the Log Archive account, Audit account, and
member accounts, for operations critical to maintaining the landing zone, such as
notifying you of drifted resources.

The `AWSServiceRoleForAWSControlTower` role requires an attached managed
policy and a role trust policy for the IAM role.

**Managed policy for this role:** `AWSControlTowerAccountServiceRolePolicy`

Role trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "controltower.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## AWSControlTowerAccountServiceRolePolicy

This AWS-managed policy allows AWS Control Tower to call AWS services that provide
automated account configuration and centralized governance on your behalf.

The policy contains the minimum permissions for AWS Control Tower to implement AWS Security Hub CSPM
findings forwarding for resources managed by Security Hub CSPM controls that are part of the
**Security Hub CSPM Service-managed Standard: AWS Control Tower**, and it prevents
changes that restrict the ability to manage customer accounts. It is part of background
AWS Security Hub CSPM drift detection process that is not directly initiated by a customer.

The policy gives permissions to create Amazon EventBridge rules, specifically for Security Hub CSPM
controls, in each member account, and these rules must specify an exact EventPattern.
Also, a rule can operate only on rules managed by our service principal.

**Service principal:**
`controltower.amazonaws.com`

For more information, see [AWSControlTowerAccountServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSControlTowerAccountServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSControlTowerAccountServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

Updates to this managed policy are summarized in the table, [Managed policies for AWS Control Tower](managed-policies-table.md "managed-policies-table.md").
