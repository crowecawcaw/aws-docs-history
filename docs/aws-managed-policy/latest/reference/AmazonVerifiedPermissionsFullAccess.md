

# AmazonVerifiedPermissionsFullAccess
<a name="AmazonVerifiedPermissionsFullAccess"></a>

**Description**: Provides full access to Verified Permissions

`AmazonVerifiedPermissionsFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonVerifiedPermissionsFullAccess-how-to-use"></a>

You can attach `AmazonVerifiedPermissionsFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonVerifiedPermissionsFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 11, 2024, 18:19 UTC 
+ **Edited time:** October 11, 2024, 18:19 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonVerifiedPermissionsFullAccess`

## Policy version
<a name="AmazonVerifiedPermissionsFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonVerifiedPermissionsFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AccountLevelPermissions",
      "Effect" : "Allow",
      "Action" : [
        "verifiedpermissions:CreatePolicyStore",
        "verifiedpermissions:ListPolicyStores"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "PolicyStoreLevelPermissions",
      "Effect" : "Allow",
      "Action" : [
        "verifiedpermissions:*"
      ],
      "Resource" : [
        "arn:aws:verifiedpermissions::*:policy-store/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonVerifiedPermissionsFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)