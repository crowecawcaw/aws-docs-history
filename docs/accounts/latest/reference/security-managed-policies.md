# AWS managed policies for AWS Account Management

###### AWS Account Management currently provides two AWS managed policies that are

available for your use:

- [AWSAccountManagementReadOnlyAccess](#security-managed-policies-AWSAccountManagementReadOnlyAccess "#security-managed-policies-AWSAccountManagementReadOnlyAccess")
- [AWSAccountManagementFullAccess](#security-managed-policies-AWSAccountManagementFullAccess "#security-managed-policies-AWSAccountManagementFullAccess")
- [Policy updates](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
  An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
  to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AWSAccountManagementReadOnlyAccess

You can attach the `AWSAccountManagementReadOnlyAccess` policy to your
IAM identities.

This policy provides read-only permissions to only view the following:

- The metadata about your AWS accounts
- The AWS Regions that are enabled or disabled for the AWS account (you can
  view status of Regions in your account only by using the AWS console)

It does this by granting permission to run any of the `Get*` or
`List*` operations. It doesn't provide any ability to modify the account
metadata or enable or disable AWS Regions for the account.

###### Permissions details

This policy includes the following permissions.

- `account` – Allows principals to retrieve the metadata
  information about AWS accounts. It also allows principals to list the
  AWS Regions that are enabled for the account in the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "account:Get*",
 "account:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSAccountManagementFullAccess

You can attach the `AWSAccountManagementFullAccess` policy to your IAM
identities.

This policy provides full administrative access to view or modify the
following:

- The metadata about your AWS accounts
- The AWS Regions that are enabled or disabled for the AWS account (you can
  view status or enable or disable Regions for your account only by using the
  AWS console)

It does this by granting permission to run any `account` operations.

###### Permissions details

This policy includes the following permissions.

- `account` – Allows principals to view or modify the metadata
  information about AWS accounts. It also allows principals to list the
  AWS Regions that are enabled for the account and enable or disable them in the
  AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "account:*",
 "Resource": "*"
 }
 ]
}`

```

## Account Management updates to AWS managed policies

View details about updates to AWS managed policies for Account Management since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Account Management Document history page.

| Change                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                             | Date          |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| AWS Account Management launched with new AWS managed policies and started<br>tracking changes | Account Management initially launched with the following AWS managed<br>policies:<br>• [AWSAccountManagementReadOnlyAccess](#security-managed-policies-AWSAccountManagementReadOnlyAccess "#security-managed-policies-AWSAccountManagementReadOnlyAccess")<br>• [AWSAccountManagementFullAccess](#security-managed-policies-AWSAccountManagementFullAccess "#security-managed-policies-AWSAccountManagementFullAccess") | Sept 30, 2021 |
