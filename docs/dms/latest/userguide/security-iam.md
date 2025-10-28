# Identity and access management for AWS Database Migration Service

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS DMS resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How AWS Database Migration Service works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [AWS Database Migration Service identity-based
  policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Resource-based policy
  examples for AWS KMS](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md")
- [Using secrets to access AWS Database Migration Service
  endpoints](security_iam_secretsmanager.md "security_iam_secretsmanager.md")
- [Using service-linked roles for
  AWS DMS](using-service-linked-roles.md "using-service-linked-roles.md")
- [Troubleshooting AWS Database Migration Service identity
  and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")
- [IAM permissions needed to use
  AWS DMS](#CHAP_Security.IAMPermissions "#CHAP_Security.IAMPermissions")
- [Creating the IAM roles to use with AWS DMS](#CHAP_Security.APIRole "#CHAP_Security.APIRole")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [AWS managed policies for AWS Database Migration Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting AWS Database Migration Service identity
  and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How AWS Database Migration Service works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [AWS Database Migration Service identity-based
  policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based

policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based

policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Access control lists (ACLs)

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC
are examples of services that support ACLs. To learn more about ACLs, see [Access control list (ACL)
overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service Developer Guide_.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy

types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

## IAM permissions needed to use

AWS DMS

You use certain IAM permissions and IAM roles to use AWS DMS. If you are signed in as an
IAM user and want to use AWS DMS, your account administrator must attach the policy
discussed in this section to the IAM user, group, or role that you use to run AWS DMS. For
more information about IAM permissions, see the [IAM User Guide](../../../IAM/latest/UserGuide/introduction_access-management.md "../../../IAM/latest/UserGuide/introduction_access-management.md").

The following policy gives you access to AWS DMS, and also permissions for certain
actions needed from other Amazon services such as AWS KMS, IAM, Amazon EC2, and Amazon CloudWatch. CloudWatch
monitors your AWS DMS migration in real time and collects and tracks metrics that
indicate the progress of your migration. You can use CloudWatch Logs to debug problems
with a task.

###### Note

You can further restrict access to AWS DMS resources using tagging. For more
information about restricting access to AWS DMS resources using tagging, see [Fine-grained access control
using resource names and tags](CHAP_Security.md "CHAP_Security.md").

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
 "iam:PassRole",
 "iam:CreateRole",
 "iam:AttachRolePolicy"
 ],
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

The breakdown of these following permissions might help you better understand why each
one is necessary.

The following section is required to allow the user to call AWS DMS API
operations.

```
{
            "Effect": "Allow",
            "Action": "dms:*",
            "Resource": "arn:aws:dms:`region`:`account`:`resourcetype`/`id`"
}
```

The following section is required to allow the user to list their available AWS KMS keys
and alias for display in the console. This entry is not required if you know the Amazon
Resource Name (ARN) for the KMS key and you are using only the AWS Command Line Interface (AWS CLI).

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

The following section is required for certain endpoint types that require an IAM role
ARN to be passed in with the endpoint. In addition, if the required AWS DMS roles
aren't created ahead of time, the AWS DMS console can create the role. If all roles
are configured ahead of time, all that is required is `iam:GetRole` and
`iam:PassRole`. For more information about roles, see [Creating the IAM roles to use with AWS DMS](#CHAP_Security.APIRole "#CHAP_Security.APIRole").

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

The following section is required because AWS DMS needs to create the Amazon EC2 instance and
configure the network for the replication instance that is created. These resources
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
information about adding these roles, see [Creating the IAM roles to use with AWS DMS](#CHAP_Security.APIRole "#CHAP_Security.APIRole").

## Creating the IAM roles to use with AWS DMS

If you use the AWS DMS console, the AWS CLI or the AWS DMS API for your database migration, you must add
three IAM roles to your AWS account before you can use the features of AWS DMS. Two
of these are `dms-vpc-role` and `dms-cloudwatch-logs-role`. If you
use Amazon Redshift as a target database, you must also add the IAM role
`dms-access-for-endpoint` to your AWS account.

Updates to managed policies are automatic. If you are using a custom policy with the
IAM roles, be sure to periodically check for updates to the managed policy in this
documentation. You can view the details of the managed policy by using a combination of
the `get-policy` and `get-policy-version` commands.

For example, the following `get-policy` command retrieves information about
the specified IAM role.

```

aws iam get-policy --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole

```

The information returned from the command is as follows.

```

{
    "Policy": {
        "PolicyName": "AmazonDMSVPCManagementRole",
        "PolicyId": "ANPAJHKIGMBQI4AEFFSYO",
        "Arn": "arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole",
        "Path": "/service-role/",
        "DefaultVersionId": "v4",
        "AttachmentCount": 1,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "Description": "Provides access to manage VPC settings for AWS managed customer configurations",
        "CreateDate": "2015-11-18T16:33:19+00:00",
        "UpdateDate": "2024-07-25T15:19:01+00:00",
        "Tags": []
    }
}

```

The following `get-policy-version` command retrieves IAM policy
information.

```

aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole --version-id v4

```

The information returned from the command is as follows.

```

{
    "PolicyVersion": {
        "Document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DescribeAvailabilityZones",
                        "ec2:DescribeDhcpOptions",
                        "ec2:DescribeInternetGateways",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:ModifyNetworkInterfaceAttribute"
                    ],
                    "Resource": "*"
                }
            ]
        },
        "VersionId": "v4",
        "IsDefaultVersion": true,
        "CreateDate": "2024-07-25T15:19:01+00:00"
    }
}

```

You can use the same commands to get information about
`AmazonDMSCloudWatchLogsRole` and the
`AmazonDMSRedshiftS3Role` managed policy.

The following procedures create the `dms-vpc-role`,
`dms-cloudwatch-logs-role`, and `dms-access-for-endpoint` IAM
roles.

###### To create the dms-vpc-role IAM role for use with the AWS CLI or

AWS DMS API

1. Create a JSON file with the following IAM policy. Name the JSON file
   `dmsAssumeRolePolicyDocument.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Create the role using the AWS CLI using the following command.

```

aws iam create-role --role-name dms-vpc-role --assume-role-policy-document file://dmsAssumeRolePolicyDocument.json

```

2. Attach the `AmazonDMSVPCManagementRole` policy to
   `dms-vpc-role` using the following command.

```

aws iam attach-role-policy --role-name dms-vpc-role --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole

```

###### To create the dms-cloudwatch-logs-role IAM role for use with the

AWS CLI or AWS DMS API

1. Create a JSON file with the following IAM policy. Name the JSON file
   `dmsAssumeRolePolicyDocument2.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Create the role using the AWS CLI using the following command.

```

aws iam create-role --role-name dms-cloudwatch-logs-role --assume-role-policy-document file://dmsAssumeRolePolicyDocument2.json

```

2. Attach the `AmazonDMSCloudWatchLogsRole` policy to
   `dms-cloudwatch-logs-role` using the following command.

```

aws iam attach-role-policy --role-name dms-cloudwatch-logs-role --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole

```

If you use Amazon Redshift as your target database, you must create the IAM role
`dms-access-for-endpoint` to provide access to Amazon S3.

###### To create the dms-access-for-endpoint IAM role for use with Amazon Redshift as

a target database

1. Create a JSON file with the following IAM policy. Name the JSON file
   `dmsAssumeRolePolicyDocument3.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "1",
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Sid": "2",
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Create the role using the AWS CLI using the following command.

```

  aws iam create-role --role-name dms-access-for-endpoint --assume-role-policy-document file://dmsAssumeRolePolicyDocument3.json

```

3. Attach the `AmazonDMSRedshiftS3Role` policy to
   `dms-access-for-endpoint` role using the following
   command.

```

aws iam attach-role-policy --role-name dms-access-for-endpoint \
    --policy-arn arn:aws:iam::aws:policy/service-role/AmazonDMSRedshiftS3Role
```

You should now have the IAM policies in place to use the AWS CLI or AWS DMS
API.
