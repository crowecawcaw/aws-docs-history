# Resource-based

policy examples for AWS Organizations

The following code examples show how you can use resource-based delegation policies. For more information, see [Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

###### Topics

- [View organization, OUs, accounts, and policies](#orgs_delegate_policies_example_view_accts_orgs "#orgs_delegate_policies_example_view_accts_orgs")
- [Create, read, update, and delete policies](#orgs_delegate_policies_example_crud_policies "#orgs_delegate_policies_example_crud_policies")
- [Tag and untag policies](#orgs_delegate_policies_example_tag_untag_policies "#orgs_delegate_policies_example_tag_untag_policies")
- [Attach policies to a single OU or account](#orgs_delegate_policies_example_attach_policies "#orgs_delegate_policies_example_attach_policies")
- [Consolidated permissions to manage an organization's backup policies](#orgs_delegate_policies_example_consolidate_permissions "#orgs_delegate_policies_example_consolidate_permissions")

## Example: View organization, OUs, accounts, and policies

Before delegating the management of policies, you must delegate the permissions to navigate the structure of an organization and see the organizational units (OUs), accounts, and the policies attached to them.

This example shows how you might include these permissions in your resource-based delegation policy for the member account, `AccountId`.

###### Important

It is advisable that you include permissions to only the minimum required actions as shown in the example, although it's possible to delegate any Organizations read-only action using this policy.

This example delegation policy grants the permissions necessary to complete actions
programmatically from the AWS API or AWS CLI. To use this delegation policy, replace the
AWS [placeholder text](orgs_getting-started_concepts.md "orgs_getting-started_concepts.md") for `AccountId` with your own information. Then, follow
the directions in [Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegatingNecessaryDescribeListActions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:DescribePolicy",
 "organizations:DescribeEffectivePolicy",
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListTargetsForPolicy",
 "organizations:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Create, read, update, and delete policies

You can create a resource-based delegation policy that allows the management account to delegate `create`, `read`, `update`, and `delete` actions for any policy type.
This example shows how you might delegate these actions for service control policies to the member account, `MemberAccountId`. The two resources shown in the example grant access
to customer managed and AWS managed service control policies respectively.

###### Important

This policy allows delegated administrators to perform specified actions on policies
created by any account in the organization, including the management account.

It doesn't allow delegated administrators to attach or detach policies because it doesn't include the permissions required to perform `organizations:AttachPolicy`
and `organizations:DetachPolicy` actions.

This example delegation policy grants the permissions necessary to complete actions
programmatically from the AWS API or AWS CLI. Replace the AWS placeholder text for
`MemberAccountId`, `ManagementAccountId`, and `OrganizationId` with your own information. Then, follow the directions in
[Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegatingDescribeListActionsWithoutCondition",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DelegatingPolicyActionsWithCondition",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribePolicy",
 "organizations:DescribeEffectivePolicy",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListTargetsForPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "organizations:PolicyType": "SERVICE_CONTROL_POLICY"
 }
 }
 },
 {
 "Sid": "DelegatingMinimalActionsForSCPs",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:CreatePolicy",
 "organizations:DescribePolicy",
 "organizations:UpdatePolicy",
 "organizations:DeletePolicy"
 ],
 "Resource": [
 "arn:aws:organizations::`111122223333`:policy/o-`OrganizationId`/service_control_policy/*",
 "arn:aws:organizations::aws:policy/service_control_policy/*"
 ]
 }
 ]
}`

```

## Example: Tag and untag policies

This example shows how you might create a resource-based delegation policy that allows delegated administrators to tag or untag backup policies.
It grants the permissions necessary to complete actions programmatically from the AWS API or AWS CLI.

To use this delegation policy, replace the AWS
placeholder text for `MemberAccountId`, `ManagementAccountId`, and `OrganizationId` with your own information. Then, follow the directions in
[Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegatingNecessaryDescribeListActionsWithoutCondition",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DelegatingNecessaryDescribeListActionsWithCondition",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribePolicy",
 "organizations:DescribeEffectivePolicy",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListTargetsForPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "organizations:PolicyType": "BACKUP_POLICY"
 }
 }
 },
 {
 "Sid": "DelegatingTaggingBackupPolicies",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:TagResource",
 "organizations:UntagResource"
 ],
 "Resource": "arn:aws:organizations::`111122223333`:policy/o-`OrganizationId`/backup_policy/*"
 }
 ]
}`

```

## Example: Attach policies to a single OU or account

This example shows how you might create a resource-based delegation policy that allows delegated administrators to `attach` or `detach` Organizations policies from a specified organizational unit (OU) or a specified account.
Before delegating these actions, you must delegate the permissions to navigate the structure of an organization and see the accounts under it. For details, see [Example: View organization, OUs, accounts, and policies](#orgs_delegate_policies_example_view_accts_orgs "#orgs_delegate_policies_example_view_accts_orgs")

###### Important

- While this policy allows attaching or detaching policies from the specified OU or account, it excludes child OUs and accounts under child OUs.
- This policy allows delegated administrators to perform the specified actions on policies created by any account in the organization, including the management account.

This example delegation policy grants the permissions necessary to complete actions
programmatically from the AWS API or AWS CLI. To use this delegation policy, replace the
AWS placeholder text for `MemberAccountId`, `ManagementAccountId`, `OrganizationId`, and `TargetAccountId`
with your own information. Then, follow the directions in [Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegatingNecessaryDescribeListActions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:DescribePolicy",
 "organizations:DescribeEffectivePolicy",
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListTargetsForPolicy",
 "organizations:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AttachDetachPoliciesSpecifiedAccountOU",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:AttachPolicy",
 "organizations:DetachPolicy"
 ],
 "Resource": [
 "arn:aws:organizations::`111122223333`:ou/o-`OrganizationId`/ou-OUId",
 "arn:aws:organizations::`111122223333`:account/o-`OrganizationId`/`TargetAccountId`",
 "arn:aws:organizations::`111122223333`:policy/o-`OrganizationId`/backup_policy/*"
 ]
 }
 ]
}`

```

To delegate attaching and detaching policies to any OU or account in the organizations,
replace the resource in the previous example with the following resources:

```
`"Resource": [
 "arn:aws:organizations::`ManagementAccountId`:ou/o-`OrganizationId`/*",
 "arn:aws:organizations::`ManagementAccountId`:account/o-`OrganizationId`/*",
 "arn:aws:organizations::`ManagementAccountId`:policy/o-`OrganizationId`/backup_policy/*"
]`
```

## Example: Consolidated permissions to manage an organization's backup policies

This example shows how you might create a resource-based delegation policy that allows the management account to delegate full permissions necessary
to manage backup policies within the organization, including `create`, `read`, `update`, and `delete` actions, as
well as `attach` and `detach` policy actions.

###### Important

This policy allows delegated administrators to perform the specified actions on policies created by any account in the organization, including the management account.

This example delegation policy grants the permissions necessary to complete actions
programmatically from the AWS API or AWS CLI. To use this delegation policy, replace the AWS
[placeholder
text](orgs_getting-started_concepts.md "orgs_getting-started_concepts.md") for `MemberAccountId`,
`ManagementAccountId`, `OrganizationId`, and
`RootId` with your own information. Then, follow the directions in
[Delegated administrator for AWS Organizations](orgs_delegate_policies.md "orgs_delegate_policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegatingNecessaryDescribeListActions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DelegatingNecessaryDescribeListActionsForSpecificPolicyType",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:DescribePolicy",
 "organizations:DescribeEffectivePolicy",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListTargetsForPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "organizations:PolicyType": "BACKUP_POLICY"
 }
 }
 },
 {
 "Sid": "DelegatingAllActionsForBackupPolicies",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "organizations:CreatePolicy",
 "organizations:UpdatePolicy",
 "organizations:DeletePolicy",
 "organizations:AttachPolicy",
 "organizations:DetachPolicy",
 "organizations:EnablePolicyType",
 "organizations:DisablePolicyType"
 ],
 "Resource": [
 "arn:aws:organizations::`111122223333`:root/o-`OrganizationId`/r-`RootId`",
 "arn:aws:organizations::`111122223333`:ou/o-`OrganizationId`/*",
 "arn:aws:organizations::`111122223333`:account/o-`OrganizationId`/*",
 "arn:aws:organizations::`111122223333`:policy/o-`OrganizationId`/backup_policy/*"
 ],
 "Condition": {
 "StringLikeIfExists": {
 "organizations:PolicyType": "BACKUP_POLICY"
 }
 }
 }
 ]
}`

```
