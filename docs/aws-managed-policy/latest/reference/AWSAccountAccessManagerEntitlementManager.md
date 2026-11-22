

# AWSAccountAccessManagerEntitlementManager

**Description**: Provides access to manage entitlements in AWS Account Access Manager, including creating, deleting, and viewing entitlements for existing applications, along with the read access needed to look up applications, identities, and organization details.

`AWSAccountAccessManagerEntitlementManager` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAccountAccessManagerEntitlementManager-how-to-use"></a>

You can attach `AWSAccountAccessManagerEntitlementManager` to your users, groups, and roles.

## Policy details
<a name="AWSAccountAccessManagerEntitlementManager-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 18, 2026, 21:37 UTC 
+ **Edited time:** November 18, 2026, 21:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSAccountAccessManagerEntitlementManager`

## Policy version
<a name="AWSAccountAccessManagerEntitlementManager-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAccountAccessManagerEntitlementManager-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AccountAccessManagerEntitlementPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:CreateEntitlement",
        "account-access:DeleteEntitlement",
        "account-access:GetEntitlement",
        "account-access:ListEntitlements"
      ],
      "Resource" : "arn:aws:account-access:*:*:application/*"
    },
    {
      "Sid" : "AccountAccessManagerApplicationReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:GetApplication",
        "account-access:ListTagsForResource"
      ],
      "Resource" : "arn:aws:account-access:*:*:application/*"
    },
    {
      "Sid" : "AccountAccessManagerListApplicationsPermissions",
      "Effect" : "Allow",
      "Action" : "account-access:ListApplications",
      "Resource" : "*"
    },
    {
      "Sid" : "IdentityCenterListInstancesPermissions",
      "Effect" : "Allow",
      "Action" : "sso:ListInstances",
      "Resource" : "*"
    },
    {
      "Sid" : "IdentityStoreDescribePermissions",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:DescribeGroup",
        "identitystore:DescribeUser"
      ],
      "Resource" : [
        "arn:aws:identitystore::*:identitystore/*",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*"
      ]
    },
    {
      "Sid" : "IdentityStoreListPermissions",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:ListGroupMemberships",
        "identitystore:ListGroups",
        "identitystore:ListUsers"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "IdentityStoreDirectoryConsolePermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso-directory:DescribeGroup",
        "sso-directory:DescribeGroups",
        "sso-directory:DescribeUser",
        "sso-directory:DescribeUsers",
        "sso-directory:ListGroupsForUser",
        "sso-directory:ListMembersInGroup",
        "sso-directory:SearchGroups",
        "sso-directory:SearchUsers"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "OrganizationsAccountReadPermissions",
      "Effect" : "Allow",
      "Action" : "organizations:DescribeAccount",
      "Resource" : "arn:aws:organizations::*:account/o-*/*"
    },
    {
      "Sid" : "OrganizationsParentReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListAccountsForParent",
        "organizations:ListOrganizationalUnitsForParent"
      ],
      "Resource" : [
        "arn:aws:organizations::*:root/o-*/r-*",
        "arn:aws:organizations::*:ou/o-*/ou-*"
      ]
    },
    {
      "Sid" : "OrganizationsReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListRoots"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSAccountAccessManagerEntitlementManager-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)