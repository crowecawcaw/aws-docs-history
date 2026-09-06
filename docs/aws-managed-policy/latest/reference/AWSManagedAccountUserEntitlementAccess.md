

# AWSManagedAccountUserEntitlementAccess
<a name="AWSManagedAccountUserEntitlementAccess"></a>

**Description**: Grants AWS permissions to manage account access entitlements for AWS managed accounts

`AWSManagedAccountUserEntitlementAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSManagedAccountUserEntitlementAccess-how-to-use"></a>

You can attach `AWSManagedAccountUserEntitlementAccess` to your users, groups, and roles.

## Policy details
<a name="AWSManagedAccountUserEntitlementAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 17, 2026, 21:42 UTC 
+ **Edited time:** July 17, 2026, 21:42 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSManagedAccountUserEntitlementAccess`

## Policy version
<a name="AWSManagedAccountUserEntitlementAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSManagedAccountUserEntitlementAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : [
      "identitystore:CreateGroup",
      "identitystore:GetGroupId",
      "identitystore:GetUserId",
      "identitystore:CreateGroupMembership",
      "sso:ListInstances",
      "sso-directory:ListProvisioningTenants",
      "account-access:ListApplications",
      "account-access:CreateEntitlement",
      "account-access:ListEntitlements"
    ],
    "Resource" : "*"
  }
}
```

## Learn more
<a name="AWSManagedAccountUserEntitlementAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)