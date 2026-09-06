

# AWSManagedAccountManagementAccess
<a name="AWSManagedAccountManagementAccess"></a>

**Description**: Grants AWS permissions to update and maintain AWS managed roles for AWS managed accounts

`AWSManagedAccountManagementAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSManagedAccountManagementAccess-how-to-use"></a>

You can attach `AWSManagedAccountManagementAccess` to your users, groups, and roles.

## Policy details
<a name="AWSManagedAccountManagementAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 20, 2026, 19:57 UTC 
+ **Edited time:** July 20, 2026, 19:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSManagedAccountManagementAccess`

## Policy version
<a name="AWSManagedAccountManagementAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSManagedAccountManagementAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : [
      "iam:AttachRolePolicy",
      "iam:CreateRole",
      "iam:DeleteRole",
      "iam:DeleteRolePermissionsBoundary",
      "iam:DeleteRolePolicy",
      "iam:DetachRolePolicy",
      "iam:PutRolePermissionsBoundary",
      "iam:PutRolePolicy",
      "iam:TagRole",
      "iam:UntagRole",
      "iam:UpdateAssumeRolePolicy",
      "iam:UpdateRole"
    ],
    "Resource" : "arn:*:iam::*:role/managed/*"
  }
}
```

## Learn more
<a name="AWSManagedAccountManagementAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)