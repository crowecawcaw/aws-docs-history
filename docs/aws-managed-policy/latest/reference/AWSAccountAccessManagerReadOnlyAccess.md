

# AWSAccountAccessManagerReadOnlyAccess

**Description**: Provides read-only access to AWS Account Access Manager, including viewing Account Access Manager applications and entitlements and the information from IAM Identity Center, Identity Store, and AWS Organizations.

`AWSAccountAccessManagerReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAccountAccessManagerReadOnlyAccess-how-to-use"></a>

You can attach `AWSAccountAccessManagerReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSAccountAccessManagerReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 18, 2026, 21:27 UTC 
+ **Edited time:** November 18, 2026, 21:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSAccountAccessManagerReadOnlyAccess`

## Policy version
<a name="AWSAccountAccessManagerReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAccountAccessManagerReadOnlyAccess-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AccountAccessManagerReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:GetApplication",
        "account-access:GetEntitlement",
        "account-access:ListEntitlements",
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
      "Sid" : "IdentityCenterReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso:DescribeApplication",
        "sso:DescribeInstance"
      ],
      "Resource" : [
        "arn:aws:sso:::instance/*",
        "arn:aws:sso::*:application/*/*"
      ]
    },
    {
      "Sid" : "IdentityCenterListPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso:DescribeRegion",
        "sso:ListInstances"
      ],
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
      "Sid" : "KMSConsoleDescribeKeyPermissions",
      "Effect" : "Allow",
      "Action" : "kms:DescribeKey",
      "Resource" : "arn:aws:kms:*:*:key/*"
    },
    {
      "Sid" : "KMSConsoleListAliasesPermissions",
      "Effect" : "Allow",
      "Action" : "kms:ListAliases",
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
<a name="AWSAccountAccessManagerReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)