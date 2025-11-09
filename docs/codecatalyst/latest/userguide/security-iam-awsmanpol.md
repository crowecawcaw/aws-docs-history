Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# AWS managed policies for Amazon CodeCatalyst

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

## AWS managed policy: AmazonCodeCatalystSupportAccess

This is a policy that grants permissions for all space administrators and space members to
utilize the Business or Enterprise premium support plan associated with the space billing
account. These permissions allow space administrators and members to utilitze the premium
support plan for the resources they have permissions to within CodeCatalyst permissions
policies.

**Permissions details**

This policy includes the following permissions.

- `support` – Grants permissions to allow users to search for, create,
  and resolve AWS Support cases. Also grants permissions to describe communications,
  severity levels, attachments, and related support case details.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "support:DescribeAttachment",
 "support:DescribeCaseAttributes",
 "support:DescribeCases",
 "support:DescribeCommunications",
 "support:DescribeIssueTypes",
 "support:DescribeServices",
 "support:DescribeSeverityLevels",
 "support:DescribeSupportLevel",
 "support:SearchForCases",
 "support:AddAttachmentsToSet",
 "support:AddCommunicationToCase",
 "support:CreateCase",
 "support:InitiateCallForCase",
 "support:InitiateChatForCase",
 "support:PutCaseAttributes",
 "support:RateCaseCommunication",
 "support:ResolveCase"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonCodeCatalystFullAccess

This is a policy that grants permissions to manage your CodeCatalyst space and connected
accounts in the Amazon CodeCatalyst Spaces page in the AWS Management Console. This application is used to
configure AWS accounts that are connected to your space in CodeCatalyst.

**Permissions details**

This policy includes the following permissions.

- `codecatalyst` – Grants full permissions to the
  Amazon CodeCatalyst Spaces page in the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeCatalystResourceAccess",
 "Effect": "Allow",
 "Action": [
 "codecatalyst:*",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeCatalystAssociateIAMRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "codecatalyst.amazonaws.com",
 "codecatalyst-runner.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS managed

policy: AmazonCodeCatalystReadOnlyAccess

This is a policy that grants permissions to view and list information for spaces
and connected accounts in the Amazon CodeCatalyst Spaces page in the AWS Management Console. This application is
used to configure AWS accounts that are connected to your space in CodeCatalyst.

**Permissions details**

This policy includes the following permissions.

- `codecatalyst` – Grants read-only permissions to the
  Amazon CodeCatalyst Spaces page in the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecatalyst:Get*",
 "codecatalyst:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy

You can't attach AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy; to your IAM
entities. This policy is attached to a service-linked role that allows CodeCatalyst to perform
actions on your behalf. For more information, see [Using service-linked roles for
CodeCatalyst](using-service-linked-roles.md "using-service-linked-roles.md").

This policy allows customers to view application instance profiles and associated
directory users and groups when managing spaces in CodeCatalyst. Customers will view these
resources when managing spaces that support identity federation and SSO users and
groups.

**Permissions details**

This policy includes the following permissions.

- `sso` – Grants permissions to allow users to view application
  instance profiles that are managed in IAM Identity Center for associated spaces in
  CodeCatalyst.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy",
 "Effect": "Allow",
 "Action": [
 "sso:ListInstances",
 "sso:ListApplications",
 "sso:ListApplicationAssignments",
 "sso:DescribeInstance",
 "sso:DescribeApplication"
 ],
 "Resource": "*"
 }
 ]
}`

```

## CodeCatalyst updates to AWS managed

policies

View details about updates to AWS managed policies for CodeCatalyst since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the CodeCatalyst [Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                     | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy](#security-iam-awsmanpol-AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy "#security-iam-awsmanpol-AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy") – New policy | CodeCatalyst added the policy.<br>Grants permissions to allow CodeCatalyst users to view application instance<br>profiles and associated directory users and groups.                            | November 17, 2023 |
| [AmazonCodeCatalystSupportAccess](#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess "#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess") – New policy                                                                                                                                              | CodeCatalyst added the policy.<br>Grants permissions to allow CodeCatalyst users to search for, create, and<br>resolve support cases, as well as viewing related communications and<br>details. | April 20, 2023    |
| [AmazonCodeCatalystFullAccess](#security-iam-awsmanpol-AmazonCodeCatalystFullAccess "#security-iam-awsmanpol-AmazonCodeCatalystFullAccess") – New policy                                                                                                                                                       | CodeCatalyst added the policy.<br>Grants full access to CodeCatalyst.                                                                                                                           | April 20, 2023    |
| [AmazonCodeCatalystReadOnlyAccess](#security-iam-awsmanpol-AmazonCodeCatalystReadOnlyAccess "#security-iam-awsmanpol-AmazonCodeCatalystReadOnlyAccess") – New policy                                                                                                                                           | CodeCatalyst added the policy.<br>Grants read-only access to CodeCatalyst.                                                                                                                      | April 20, 2023    |
| CodeCatalyst started tracking changes                                                                                                                                                                                                                                                                          | CodeCatalyst started tracking changes for its AWS managed policies.                                                                                                                             | April 20, 2023    |
