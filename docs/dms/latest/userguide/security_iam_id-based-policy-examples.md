# AWS Database Migration Service identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
AWS DMS resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  AWS DMS console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Accessing one
  Amazon S3 bucket](#security_iam_id-based-policy-examples-access-one-bucket "#security_iam_id-based-policy-examples-access-one-bucket")
- [Accessing
  AWS DMS resources based on tags](#security_iam_id-based-policy-examples-access-resources-tags "#security_iam_id-based-policy-examples-access-resources-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS DMS resources in your
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

## Using the

AWS DMS console

The following policy gives you access to AWS DMS, including the AWS DMS
console, and also specifies permissions for certain actions needed from other Amazon
services such as Amazon EC2.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dms:*",
 "Resource": "arn:aws:dms:*:123456789012:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:*:123456789012:key/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:CreateRole",
 "iam:AttachRolePolicy"
 ],
 "Resource": "arn:aws:iam::123456789012:role/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "dms.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:Get*",
 "cloudwatch:List*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:FilterLogEvents",
 "logs:GetLogEvents"
 ],
 "Resource": "arn:aws:logs:*:123456789012:*"
 }
 ]
}`

```

A breakdown of these permissions might help you better understand why each one
required for using the console is necessary.

The following section is required to allow the user to list their available AWS KMS
keys and alias for display in the console. This entry is not required if you know the
Amazon Resource Name (ARN) for the KMS key and you are using only the AWS Command Line Interface
(AWS CLI).

```
{
            "Effect": "Allow",
            "Action": [
                "kms:ListAliases",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:`service`:`region`:`account`:`resourcetype`/`id`"
        }
```

The following section is required for certain endpoint types that require a role ARN
to be passed in with the endpoint. In addition, if the required AWS DMS roles aren't
created ahead of time, the AWS DMS console has the ability to create the role. If all
roles are configured ahead of time, all that is required in `iam:GetRole` and
`iam:PassRole`. For more information about roles, see [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").

```
{
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:PassRole",
                "iam:CreateRole",
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:`service`:`region`:`account`:`resourcetype`/`id`"
        }
```

The following section is required because AWS DMS needs to create the Amazon EC2 instance
and configure the network for the replication instance that is created. These resources
exist in the customer's account, so the ability to perform these actions on behalf of
the customer is required.

```
{
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcs",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:ModifyNetworkInterfaceAttribute",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "arn:aws:`service`:`region`:`account`:`resourcetype`/`id`"
        }
```

The following section is required to allow the user to be able to view replication
instance metrics.

```
{
            "Effect": "Allow",
            "Action": [
                "cloudwatch:Get*",
                "cloudwatch:List*"
            ],
            "Resource": "arn:aws:`service`:`region`:`account`:`resourcetype`/`id`"
        }
```

This section is required to allow the user to view replication logs.

```
{
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:FilterLogEvents",
                "logs:GetLogEvents"
            ],
            "Resource": "arn:aws:`service`:`region`:`account`:`resourcetype`/`id`"
        }
```

If you use the AWS DMS console, the AWS Command Line Interface (AWS CLI) or the
AWS DMS API for your migration, you need to add several roles to your account. For more
information about adding these roles, see [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").

For more information on the requirements for using this policy to access AWS DMS,
see [IAM permissions needed to use
AWS DMS](security-iam.md#CHAP_Security.IAMPermissions "security-iam.md#CHAP_Security.IAMPermissions").

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Accessing one

Amazon S3 bucket

AWS DMS uses Amazon S3 buckets as intermediate storage for database migration.
Typically, AWS DMS manages default S3 buckets for this purpose. However, in certain
cases, especially when you use the AWS CLI or the AWS DMS API, AWS DMS enables you
to specify your own S3 bucket instead. For example, you can specify your own S3 bucket
for migrating data to an Amazon Redshift target endpoint. In this case, you need to create a role
with permissions based on the AWS-managed `AmazonDMSRedshiftS3Role`
policy.

The following example shows a version of the `AmazonDMSRedshiftS3Role`
policy. It allows AWS DMS to grant an IAM user in your AWS account access to one
of your Amazon S3 buckets. It also allows the user to add, update, and delete objects.

In addition to granting the `s3:PutObject`, `s3:GetObject`, and
`s3:DeleteObject` permissions to the user, the policy also grants the
`s3:ListAllMyBuckets`, `s3:GetBucketLocation`, and
`s3:ListBucket` permissions. These are the additional permissions required
by the console. Other permissions allow AWS DMS to manage the bucket life cycle.
Also, the `s3:GetObjectAcl` action is required to be able to copy
objects.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:DeleteBucket",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObjectVersion",
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:GetBucketAcl",
 "s3:PutBucketVersioning",
 "s3:GetBucketVersioning",
 "s3:PutLifecycleConfiguration",
 "s3:GetLifecycleConfiguration",
 "s3:DeleteBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::dms-*"
 }
 ]
}`

```

For more information on creating a role based on this policy, see [Amazon S3 bucket
settings](CHAP_Target.md#CHAP_Target.Redshift.EndpointSettings.S3Buckets "CHAP_Target.md#CHAP_Target.Redshift.EndpointSettings.S3Buckets").

## Accessing

AWS DMS resources based on tags

You can use conditions in your identity-based policy to control access to
AWS DMS resources based on tags. This example shows how you might create a
policy that allows access to all AWS DMS endpoints. However, permission is granted
only if the endpoint database tag `Owner` has the value of that user's user
name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dms:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "dms:endpoint-tag/Owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

You can attach this policy to the IAM users in your account. If a user named
`richard-roe` attempts to access an AWS DMS endpoint, the
endpoint database must be tagged `Owner=richard-roe` or
`owner=richard-roe`. Otherwise, this user is denied access. The condition
tag key `Owner` matches both `Owner` and `owner`
because condition key names are not case-sensitive. For more information, see [IAM JSON policy
elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
