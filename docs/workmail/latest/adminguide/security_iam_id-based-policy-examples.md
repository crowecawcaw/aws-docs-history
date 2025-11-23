# Amazon WorkMail identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
Amazon WorkMail resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
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
  Amazon WorkMail console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow users read-only access to Amazon WorkMail resources](#security_iam_id-based-policy-examples-read-only-access "#security_iam_id-based-policy-examples-read-only-access")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon WorkMail resources in your
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

Amazon WorkMail console

To access the Amazon WorkMail console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
Amazon WorkMail resources in your AWS account. If you create an identity-based policy
that is more restrictive than the minimum required permissions, the console won't
function as intended for entities (IAM users or roles) with that policy.

To ensure that those entities can still use the Amazon WorkMail console, also attach
the following AWS managed policy, **AmazonWorkMailFullAccess**, to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

The **AmazonWorkMailFullAccess** policy grants an IAM user full
access to Amazon WorkMail resources. This policy gives the user access to all Amazon WorkMail,
AWS Key Management Service, Amazon Simple Email Service, and AWS Directory Service operations. This also includes several Amazon EC2
operations that Amazon WorkMail needs to perform on your behalf. The `logs` and
`cloudwatch` permissions are required for email event logging, and
viewing metrics in the Amazon WorkMail console. Audit logging uses CloudWatch Logs, Amazon S3, and Amazon Data FireHose to store `logs`. For more information, see [Logging and monitoring in Amazon WorkMail](monitoring-overview.md "monitoring-overview.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "WorkMailAdministration",
 "Effect": "Allow",
 "Action": [
 "ds:AuthorizeApplication",
 "ds:CheckAlias",
 "ds:CreateAlias",
 "ds:CreateDirectory",
 "ds:CreateIdentityPoolDirectory",
 "ds:DeleteDirectory",
 "ds:DescribeDirectories",
 "ds:GetDirectoryLimits",
 "ds:ListAuthorizedApplications",
 "ds:UnauthorizeApplication",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateNetworkInterface",
 "ec2:CreateSecurityGroup",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc",
 "ec2:DeleteSecurityGroup",
 "ec2:DeleteSubnet",
 "ec2:DeleteVpc",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "kms:DescribeKey",
 "kms:ListAliases",
 "lambda:ListFunctions",
 "route53:ChangeResourceRecordSets",
 "route53:ListHostedZones",
 "route53:ListResourceRecordSets",
 "route53:GetHostedZone",
 "route53domains:CheckDomainAvailability",
 "route53domains:ListDomains",
 "ses:*",
 "workmail:*",
 "iam:ListRoles",
 "logs:DescribeLogGroups",
 "logs:CreateLogGroup",
 "logs:PutRetentionPolicy",
 "logs:DeleteDeliveryDestination",
 "logs:DeleteDeliveryDestinationPolicy",
 "logs:DescribeDeliveryDestinations",
 "logs:GetDeliveryDestination",
 "logs:GetDeliveryDestinationPolicy",
 "logs:PutDeliveryDestination",
 "logs:PutDeliveryDestinationPolicy",
 "logs:CreateDelivery",
 "logs:DeleteDelivery",
 "logs:DescribeDeliveries",
 "logs:GetDelivery",
 "logs:DeleteDeliverySource",
 "logs:DescribeDeliverySources",
 "logs:GetDeliverySource",
 "logs:PutDeliverySource",
 "logs:DescribeResourcePolicies",
 "cloudwatch:GetMetricData",
 "firehose:DescribeDeliveryStream",
 "firehose:ListDeliveryStreams",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AuditLogDeliveryThroughCWLogs",
 "Effect": "Allow",
 "Action": [
 "firehose:TagDeliveryStream",
 "logs:PutResourcePolicy",
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "InboundOutboundEmailEventsLink",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "events.workmail.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AuditLoggingLink",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "delivery.logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "InboundOutboundEmailEventsUnlink",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/events.workmail.amazonaws.com/AWSServiceRoleForAmazonWorkMailEvents*"
 },
 {
 "Sid": "InboundOutboundEmailEventsAuth",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/*workmail*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "events.workmail.amazonaws.com"
 }
 }
 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.

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

## Allow users read-only access to Amazon WorkMail resources

The following policy statement grants an IAM user read-only access to Amazon WorkMail
resources. This policy gives the same level of access as the AWS managed policy
**AmazonWorkMailReadOnlyAccess**. Either policy gives the user
access to all of the Amazon WorkMail `Describe` operations. Access to the AWS Directory Service
`DescribeDirectories` operation is needed to obtain information about
your Directory Service directories. Access to the Amazon SES service is needed to obtain information
about the configured domains. Access to AWS Key Management Service is needed to obtain information
about the used encryption keys. The `logs` and `cloudwatch`
permissions are required for email event logging and viewing metrics in the Amazon WorkMail
console. Audit logging uses CloudWatch Logs, Amazon S3, and Amazon Data FireHose to store `logs`. For more information, see [Logging and monitoring in Amazon WorkMail](monitoring-overview.md "monitoring-overview.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "WorkMailReadOnly",
 "Effect": "Allow",
 "Action": [
 "ses:Describe*",
 "ses:Get*",
 "workmail:Describe*",
 "workmail:Get*",
 "workmail:List*",
 "workmail:Search*",
 "lambda:ListFunctions",
 "iam:ListRoles",
 "logs:DescribeLogGroups",
 "logs:DescribeDeliveryDestinations",
 "logs:GetDeliveryDestination",
 "logs:GetDeliveryDestinationPolicy",
 "logs:DescribeDeliveries",
 "logs:DescribeDeliverySources",
 "logs:GetDelivery",
 "logs:GetDeliverySource",
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 }
 ]
}`

```
