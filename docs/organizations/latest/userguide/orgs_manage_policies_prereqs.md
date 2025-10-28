# Prerequisites and permissions for

management policies for AWS Organizations

This page describes the prerequisites and required permissions for management policies for AWS Organizations.

###### Topics

- [Prerequisites for management
  policies](#manage-policies-prereqs-overview "#manage-policies-prereqs-overview")
- [Permissions for management policies](#manage-policies-permissions "#manage-policies-permissions")

## Prerequisites for management

policies

Using management policies for an organization requires the following:

- Your organization must have [all features enabled](orgs_manage_org_support-all-features.md "orgs_manage_org_support-all-features.md").
- You must be signed in to your organization's management account or be a delegated administrator.
- Your AWS Identity and Access Management (IAM) user or role must have the permissions that are listed
  in the following section.

## Permissions for management policies

The following example IAM policy provides permissions to use all aspects of
management policies in an organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OrganizationPolicies",
 "Effect": "Allow",
 "Action": [
 "organizations:AttachPolicy",
 "organizations:CreatePolicy",
 "organizations:DeletePolicy",
 "organizations:DescribeAccount",
 "organizations:DescribeCreateAccountStatus",
 "organizations:DescribeEffectivePolicy",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribePolicy",
 "organizations:DetachPolicy",
 "organizations:DisableAWSServiceAccess",
 "organizations:DisablePolicyType",
 "organizations:EnableAWSServiceAccess",
 "organizations:EnablePolicyType",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListCreateAccountStatus",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListPolicies",
 "organizations:ListPoliciesForTarget",
 "organizations:ListRoots",
 "organizations:ListTargetsForPolicy",
 "organizations:UpdatePolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about IAM policies and permissions, see the
[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
