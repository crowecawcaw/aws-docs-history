# AWS managed policies for AWS RAM

AWS Resource Access Manager currently provides several AWS RAM managed policies, which are described in this
topic.

###### AWS managed policies

- [AWSResourceAccessManagerReadOnlyAccess](#security-iam-managed-policies-AWSResourceAccessManagerReadOnlyAccess "#security-iam-managed-policies-AWSResourceAccessManagerReadOnlyAccess")
- [AWSResourceAccessManagerFullAccess](#security-iam-managed-policies-AWSResourceAccessManagerFullAccess "#security-iam-managed-policies-AWSResourceAccessManagerFullAccess")
- [AWSResourceAccessManagerResourceShareParticipantAccess](#security-iam-managed-policies-AWSResourceAccessManagerResourceShareParticipantAccess "#security-iam-managed-policies-AWSResourceAccessManagerResourceShareParticipantAccess")
- [AWSResourceAccessManagerServiceRolePolicy](#security-iam-managed-policies-AWSResourceAccessManagerServiceRolePolicy "#security-iam-managed-policies-AWSResourceAccessManagerServiceRolePolicy")
- [Policy updates](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
  In the preceding list, you can attach the first three policies to your IAM roles,
  groups, and users to grant permissions. The last policy in the list is reserved for the
  AWS RAM service's service-linked role.

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

## AWS managed policy: AWSResourceAccessManagerReadOnlyAccess

You can attach the `AWSResourceAccessManagerReadOnlyAccess` policy to your
IAM identities.

This policy provides read-only permissions to the resource shares that are owned by your
AWS account.

It does this by granting permission to run any of the `Get*` or
`List*` operations. It doesn't provide any ability to modify any
resource share.

###### Permissions details

This policy includes the following permissions.

- `ram` – Allows principals to view details about resource shares owned
  by the account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ram:Get*",
 "ram:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AWSResourceAccessManagerFullAccess

You can attach the `AWSResourceAccessManagerFullAccess` policy to your
IAM identities.

This policy provides full administrative access to view or modify the resource shares that are
owned by your AWS account.

It does this by granting permission to run any `ram` operations.

###### Permissions details

This policy includes the following permissions.

- `ram` – Allows principals to view or modify any information
  about the resource shares that are owned by the AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ram:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AWSResourceAccessManagerResourceShareParticipantAccess

You can attach the `AWSResourceAccessManagerResourceShareParticipantAccess`
policy to your IAM identities.

This policy provides principals the ability to accept or reject resource shares that are shared
with this AWS account, and to view details about these resource shares. It doesn't provide any
ability to modify those resource shares.

It does this by granting permission to run some `ram` operations.

###### Permissions details

This policy includes the following permissions.

- `ram` – Allows principals to accept or reject resource share
  invitations and to view details about the resource shares that are shared with the
  account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ram:AcceptResourceShareInvitation",
 "ram:GetResourcePolicies",
 "ram:GetResourceShareInvitations",
 "ram:GetResourceShares",
 "ram:ListPendingInvitationResources",
 "ram:ListPrincipals",
 "ram:ListResources",
 "ram:RejectResourceShareInvitation"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSResourceAccessManagerServiceRolePolicy

The AWS managed policy `AWSResourceAccessManagerServiceRolePolicy`can be
used only with the service-linked role for AWS RAM. You can't attach, detach, modify, or
delete this policy.

This policy provides AWS RAM with read-only access to your organization's structure.
When you enable integration between AWS RAM and AWS Organizations, AWS RAM automatically creates a
service-linked role named [AWSServiceRoleForResourceAccessManager](https://console.aws.amazon.com/iam/home#/roles/AWSServiceRoleForResourceAccessManager "https://console.aws.amazon.com/iam/home#/roles/AWSServiceRoleForResourceAccessManager") that the service assumes when it
needs to look up information about your organization and its accounts, for example, when
you view the organization's structure in the AWS RAM console.

It does this by granting read-only permission to run the
`organizations:Describe` and `organizations:List` operations
that provide details of the organization's structure and accounts.

###### Permissions details

This policy includes the following permissions.

- `organizations` – Allows principals to view information
  about the organization's structure, including the organizational units, and the
  AWS accounts they contain.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListChildren",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListRoots"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowDeletionOfServiceLinkedRoleForResourceAccessManager",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/ram.amazonaws.com/*"
 ]
 }
 ]
}`

```

## AWS RAM updates to AWS managed

policies

View details about updates to AWS managed policies for AWS RAM since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS RAM Document history page.

| Change                                               | Description                                                                    | Date               |
| ---------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------ |
| AWS Resource Access Manager started tracking changes | AWS RAM documented its existing managed policies and started tracking changes. | September 16, 2021 |
