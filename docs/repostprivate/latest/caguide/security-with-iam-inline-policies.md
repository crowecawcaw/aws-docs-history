# Inline policies

Inline policies are policies that you create and manage. You can embed inline policies
directly into a user, group, or role. The following policy examples show how to assign
permissions to perform AWS re:Post Private actions. For general information about inline policies, see
[Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _AWS IAM User Guide_. You can use the AWS Management Console, AWS Command Line Interface (AWS CLI), or the AWS Identity and Access Management API to
create and embed inline policies.

###### Topics

- [Read-only access to re:Post Private](#read-only-access "#read-only-access")
- [Full access to re:Post Private](#full-access "#full-access")

## Read-only access to re:Post Private

The following policy grants read access to a user for IAM Identity Center and re:Post Private console. This
policy allows the user to perform re:Post Private actions that are read only.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount",

 "sso:DescribeRegisteredRegions",
 "sso:ListDirectoryAssociations",
 "sso:GetSSOStatus",
 "sso:GetManagedApplicationInstance",
 "sso:ListProfiles",
 "sso:GetProfile",
 "sso:ListProfileAssociations",

 "sso-directory:DescribeDirectory",
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups",

 "repostspace:GetSpace",
 "repostspace:ListSpaces",
 "repostspace:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Full access to re:Post Private

The following policy grants full access to a user for IAM Identity Center and re:Post Private console. This
policy allows the user to perform all re:Post Private actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount",

 "sso:DescribeRegisteredRegions",
 "sso:ListDirectoryAssociations",
 "sso:GetSSOStatus",
 "sso:GetManagedApplicationInstance",
 "sso:ListProfiles",
 "sso:GetProfile",
 "sso:ListProfileAssociations",

 "sso:CreateManagedApplicationInstance",
 "sso:DeleteManagedApplicationInstance",
 "sso:AssociateProfile",
 "sso:DisassociateProfile",

 "sso-directory:DescribeDirectory",
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups",

 "kms:ListAliases",
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:RetireGrant",

 "repostspace:*"
 ],
 "Resource": "*"
 }
 ]
}`

```
